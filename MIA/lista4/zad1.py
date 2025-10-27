
def number_of_iterations(table,index,looking_index,iteration = 1):
    if table[index] - 1 == looking_index:
        return iteration
    else:
        return number_of_iterations(table,table[index]-1,looking_index,iteration + 1)
class Zad1():
    def __init__(self):
        self.result_table = []
        self.table = []
        self.length = 0
    def load_data(self):
        self.length = int(input())
        self.table = list(map(int,input().split()))
    def fill_result_table(self):
        for i in range(self.length):
            pom_table = self.table[:]
            self.result_table.append(number_of_iterations(pom_table,i,i))
    def run(self):
        self.load_data()
        self.fill_result_table()
        self.print_result_table()
    def print_result_table(self):
        for i in self.result_table:
            print(i,end=" ")
def fun_exe():
    number_of_rows = int(input())
    for i in range(number_of_rows):
        one_example = Zad1()
        one_example.run()
        if i!= number_of_rows-1:
            print()

fun_exe()
