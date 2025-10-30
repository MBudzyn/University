def number_of_elements_less_than_number(table,number):
    begin_index = 0
    end_index = len(table) - 1
    while end_index - begin_index > 1:
        middle_index = (begin_index + end_index)//2
        if table[middle_index] <= number:
            begin_index = middle_index
        else:
            end_index = middle_index
    if table[end_index] <= number:
        return end_index + 1
    elif table[begin_index] <= number:
        return begin_index + 1
    else:
        return 0
class Zad2():
    def __init__(self):
        self.length_of_table_a = 0
        self.length_of_table_b = 0
        self.table_a = []
        self.table_b = []
        self.result = []
    def load_data(self):
        self.length_of_table_a,self.length_of_table_b = map(int,input().split())
        self.table_a = sorted(list(map(int,input().split())))
        self.table_b = list(map(int,input().split()))
    def fun(self):
        for el_b in self.table_b:
            self.result.append(number_of_elements_less_than_number(self.table_a,el_b))
    def print_result(self):
        for i in range(len(self.result) - 1):
            print(self.result[i],end=" ")
        print(self.result[len(self.result) - 1],end="")
    def run(self):
        self.load_data()
        self.fun()
        self.print_result()

zad2 = Zad2()
zad2.run()
