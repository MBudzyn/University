
def smallest_number_of_slices(table_of_hairs,max_length):
    result = 0
    during_cut = False
    for hair in table_of_hairs:
        if hair <= max_length and during_cut:
            during_cut = False
            result += 1
        if hair > max_length:
            during_cut = True
    if during_cut:
        return result + 1
    else:
        return result

class Zad2():
    def __init__(self):
        self.table_with_hairs = []
        self.number_of_hairs = 0
        self.number_of_command = 0
        self.favorite_number = 0
        self.result_table = []
        self.slices_done = False
        self.next_number_of_slices = 0
    def load_data(self):
        self.number_of_hairs,self.number_of_command,self.favorite_number = map(int,input().split())
        self.table_with_hairs = list(map(int, input().split()))
    def execute_0_command(self):
        if not self.slices_done:
            self.result_table.append(smallest_number_of_slices(self.table_with_hairs,self.favorite_number))
            self.next_number_of_slices = self.result_table[0]
            self.slices_done = True
        else:
            self.result_table.append(self.next_number_of_slices)
    def possible_situation_change(self,index_to_grow,grow_by):
        if self.table_with_hairs[index_to_grow - 1] <= self.favorite_number and self.table_with_hairs[index_to_grow - 1] + grow_by > self.favorite_number:
            return True
        else:
            return False
    def execute_1_command(self,index_to_grow,grow_by):
        if self.possible_situation_change(index_to_grow,grow_by):
            self.table_with_hairs[index_to_grow - 1] += grow_by
            if len(self.table_with_hairs) == 1:
                self.next_number_of_slices += 1
            elif index_to_grow == 1:
                if self.table_with_hairs[1] <= self.favorite_number:
                    self.next_number_of_slices += 1
            elif index_to_grow == len(self.table_with_hairs):
                if self.table_with_hairs[len(self.table_with_hairs)-2] <= self.favorite_number:
                    self.next_number_of_slices += 1
            else:
                if self.table_with_hairs[index_to_grow - 2] <= self.favorite_number and self.table_with_hairs[index_to_grow] <= self.favorite_number:
                    self.next_number_of_slices += 1
                if self.table_with_hairs[index_to_grow - 2] > self.favorite_number and self.table_with_hairs[index_to_grow] > self.favorite_number:
                    if self.next_number_of_slices > 0:
                        self.next_number_of_slices -= 1
        else:
            self.table_with_hairs[index_to_grow - 1] += grow_by

    def execute_command(self):
        pom_list = list(map(int, input().split()))
        if len(pom_list) == 1:
            self.execute_0_command()
        else:
            self.execute_1_command(pom_list[1],pom_list[2])
    def execute_all_commands(self):
        for command in range(self.number_of_command):
            self.execute_command()
    def print_result(self):
        for i in range(len(self.result_table) - 1):
            print(self.result_table[i])
        print(self.result_table[len(self.result_table) - 1], end="")

    def run(self):
        self.load_data()
        self.execute_all_commands()
        self.print_result()

zad2 = Zad2()
zad2.run()