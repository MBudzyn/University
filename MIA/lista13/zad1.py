import math
def task_condition(argument):
    if argument < 0:
        return True
    sqr = math.sqrt(argument)
    if sqr == int(sqr):
        return False
    else:
        return True
class Zad1:
    def __init__(self):
        self.number_of_data = 0
        self.table_with_data = []
        self.result = 0

    def load_data(self):
        self.number_of_data = int(input())
        self.table_with_data = list(map(int,input().split()))
        self.table_with_data.sort(reverse = True)

    def fun(self):
        for element in self.table_with_data:
            if task_condition(element):
                self.result = element
                break

    def print_result(self):
        print(self.result)

    def run(self):
        self.load_data()
        self.fun()
        self.print_result()

zad1 = Zad1()
zad1.run()
