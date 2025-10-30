class Bishop:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.table = []
    def data(self):
        rows_and_columns = input().split()
        self.rows = int(rows_and_columns[0])
        self.columns = int(rows_and_columns[1])
        for i in range(self.rows):
            self.table.append(input().split())
        for i in range(self.rows):
            for j in range(self.columns):
                self.table[i][j] = [int(self.table[i][j])]

    def first_diagonal(self):
        for i in range(self.columns):
            previous_cell = [-1]
            actual_pos_x = 0
            actual_pos_y = i
            while (actual_pos_x < self.columns and actual_pos_y < self.rows):
                if previous_cell == [-1]:
                    self.table[actual_pos_x][actual_pos_y].append(0)
                else:
                    self.table[actual_pos_x][actual_pos_y].append(previous_cell[0] + previous_cell[1])
                previous_cell = self.table[actual_pos_x][actual_pos_y]
                actual_pos_x += 1
                actual_pos_y += 1

        for i in range(self.rows):
            previous_cell = [-1]
            actual_pos_x = i + 1
            actual_pos_y = 0
            while (actual_pos_x < self.rows and actual_pos_y < self.columns):
                if previous_cell == [-1]:
                    self.table[actual_pos_x][actual_pos_y].append(0)
                else:
                    self.table[actual_pos_x][actual_pos_y].append(previous_cell[0] + previous_cell[1])
                previous_cell = self.table[actual_pos_x][actual_pos_y]
                actual_pos_x += 1
                actual_pos_y += 1

    def second_diagonal(self):
        for i in range(self.rows-1,-1,-1):
            previous_cell = [-1]
            actual_pos_x = self.rows -1
            actual_pos_y = i
            while (actual_pos_x >= 0 and actual_pos_y >= 0):
                if previous_cell == [-1]:
                    self.table[actual_pos_x][actual_pos_y].append(0)
                else:
                    self.table[actual_pos_x][actual_pos_y].append(previous_cell[0] + previous_cell[2])
                previous_cell = self.table[actual_pos_x][actual_pos_y]
                actual_pos_x -= 1
                actual_pos_y -= 1

        for i in range(self.rows - 1,-1,-1):
            previous_cell = [-1]
            actual_pos_x = i - 1
            actual_pos_y = self.rows -1
            while (actual_pos_x >= 0  and actual_pos_y >= 0):
                if previous_cell == [-1]:
                    self.table[actual_pos_x][actual_pos_y].append(0)
                else:
                    self.table[actual_pos_x][actual_pos_y].append(previous_cell[0] + previous_cell[2])
                previous_cell = self.table[actual_pos_x][actual_pos_y]
                actual_pos_x -= 1
                actual_pos_y -= 1


    def data_print(self):
        for i in self.table:
            print(i)

new = Bishop()
new.data()
new.first_diagonal()
new.second_diagonal()
new.data_print()

""""
4 4
1 2 3 4
1 5 6 7
1 3 4 5
8 9 0 1
"""
