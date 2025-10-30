import copy
def create_comb_string(number_of_ones, number_of_zeros):
    if number_of_ones <= 0:
        return ['0' * number_of_zeros]
    if number_of_zeros <= 0:
        return ['1' * number_of_ones]
    result = []
    for string in create_comb_string(number_of_ones - 1, number_of_zeros):
        result.append('1' + string)
    for string in create_comb_string(number_of_ones, number_of_zeros - 1):
        result.append('0' + string)
    return result

def parse_comb(comb_string):
    pom_result = []
    final_result = []
    pom = 0
    for char in comb_string:
        pom_result.append(int(char))
    for i in range(len(pom_result)):
        if pom_result[i] == 1:
            pom += 1
        else:
            final_result.append(pom)
            pom = 0
    final_result.append(pom)
    return final_result


class variable:
    def __init__(self, value, is_row: bool, index, length):
        self.value = value
        self.domain = []
        self.is_row = is_row
        self.index = index
        self.length = length
        self.create_domain()

    def __copy__(self):
        new_var = variable(self.value, self.is_row, self.index, self.length)
        new_var.domain = self.domain.copy()
        return new_var
    def is_domain_empty(self):
        return len(self.domain) == 0

    def reduce_domain(self, correct_value, index):
        new_domain = []
        for domain in self.domain:
            if domain[index] == correct_value:
                new_domain.append(domain)
        self.domain = new_domain

    def can_be_reduced(self, index):
        for i in range(len(self.domain) - 1):
            if self.domain[i][index] != self.domain[i + 1][index]:
                return False
        return True
    def create_domain(self):
        known = 0
        for value in self.value:
            known += value
        known += len(self.value) - 1
        unknown = len(self.value)
        fields_to_fill = self.length - known
        for comb in create_comb_string(fields_to_fill, unknown):
            pom_res = []  # Utwórz nową listę dla każdej kombinacji
            pom = parse_comb(comb)
            for i in range(len(pom) - 1):
                for _ in range(pom[i]):
                    pom_res.append(0)
                for _ in range(self.value[i]):
                    pom_res.append(1)
                pom_res.append(0)
            for _ in range(pom[-1]):
                pom_res.append(0)
            pom_res.pop()
            self.domain.append(pom_res)


class LogicalPictures:
    def __init__(self):
        self.board = []
        self.rows = {}
        self.columns = {}
        self.number_of_rows = 0
        self.number_of_columns = 0
        self.load_board('test2.txt')
        self.queue = [(i, j) for i in range(self.number_of_rows) for j in range(self.number_of_columns)]



    def every_domain_is_not_empty(self):
        for row in self.rows.values():
            if row.is_domain_empty():
                return False
        for column in self.columns.values():
            if column.is_domain_empty():
                return False
        return True

    def actualize_queue_del_row(self, row):
        for i in range(self.number_of_columns):
            if (row, i) in self.queue:
                self.queue.remove((row, i))


    def get_indeksys_with_smallest_domain(self):
        smallest_domain = 100000000
        indeksy = (0, 0)
        for i, j in self.queue:
            if self.rows[i].domain and self.columns[j].domain:
                if len(self.rows[i].domain) + len(self.columns[j].domain) < smallest_domain:
                    smallest_domain = len(self.rows[i].domain) + len(self.columns[j].domain)
                    indeksy = (i, j)
        return indeksy

    def set_row(self, row_index, row_value):
        self.rows[row_index].domain = [row_value]
        for i in range(self.number_of_columns):
            self.set_field(row_index, i, row_value[i])
        self.actualize_queue_del_row(row_index)



    def is_solved(self):
        for row in self.rows.values():
            if len(row.domain) != 1:
                return False
        for column in self.columns.values():
            if len(column.domain) != 1:
                return False
        return True

    def set_field(self, row, column, value):
        for domain in self.rows[row].domain:
            if domain[column] != value:
                self.rows[row].domain.remove(domain)
        for domain in self.columns[column].domain:
            if domain[row] != value:
                self.columns[column].domain.remove(domain)




    def load_board(self, file_name):

        with open(file_name, 'r') as f:
            lines = f.readlines()
            pom1 = list(map(int, lines[0].split()))
            self.number_of_rows = pom1[0]
            self.number_of_columns = pom1[1]
            self.board = [[0 for _ in range(self.number_of_columns)] for _ in range(self.number_of_rows)]
            for i in range(1, self.number_of_rows+1):
                row_list = (list(map(int, lines[i].split())))
                self.rows[i - 1] = variable(row_list, True, i-1, self.number_of_columns)

            for i in range(self.number_of_rows+1, self.number_of_rows + self.number_of_columns + 1):
                column_list = (list(map(int, lines[i].split())))
                self.columns[i - self.number_of_rows - 1] = variable(column_list, False, i - self.number_of_rows-1, self.number_of_rows)


    def wnioskowanie(self):
        nothing_changed_counter = 0

        while len(self.queue) > 0 and nothing_changed_counter <= len(self.queue):
            actual_relation = self.queue.pop(0)
            row_ind = actual_relation[0]
            column_ind = actual_relation[1]
            row_var = self.rows[row_ind]
            column_var = self.columns[column_ind]

            if row_var.domain and column_var.domain:  # Sprawdź, czy domeny nie są puste
                if row_var.can_be_reduced(column_ind):
                    nothing_changed_counter = 0
                    column_var.reduce_domain(row_var.domain[0][column_ind], row_ind)

                elif column_var.can_be_reduced(row_ind):
                    nothing_changed_counter = 0
                    row_var.reduce_domain(column_var.domain[0][row_ind], column_ind)

                else:
                    nothing_changed_counter +=1
                    self.queue.append(actual_relation)
            else:
                return False
        return True


    def print_data(self):
        for row in self.board:
            print(row)
        print(self.rows)
        print(self.columns)

    def fill_board(self):
        for i in range(self.number_of_rows):
            for j in range(self.number_of_columns):
                if self.rows[i].domain[0][j] == 1:
                    self.board[i][j] = '#'
                else:
                    self.board[i][j] = '.'

    def print_result_to_file(self):
        with open('zad_output.txt', 'w') as f:
            for row in self.board:
                f.write(''.join(row) + '\n')
        for row in self.board:
            print(''.join(row))

    def solve(self):
        stack = [(self, 0, 0)]
        while stack:
            actual = stack[-1][0]
            row, domain_index = stack[-1][1], stack[-1][2]
            new_actual = copy.deepcopy(actual)
            new_actual.wnioskowanie()
            if new_actual.every_domain_is_not_empty():
                if new_actual.is_solved():
                    new_actual.fill_board()
                    new_actual.print_result_to_file()
                    return
                else:
                    if domain_index < len(new_actual.rows[row].domain):
                        new_actual.set_row(row, new_actual.rows[row].domain[domain_index])
                        stack.append((new_actual, row, domain_index + 1))
                    else:
                        stack.pop()
            else:
                stack.pop()





object = LogicalPictures()
object.solve()

