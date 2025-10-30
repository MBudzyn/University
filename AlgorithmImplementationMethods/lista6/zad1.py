

def divisible_by_3(string):
    sum = 0
    for i in string:
        sum += int(i)
    if sum % 3 == 0:
        return True
    else:
        return False
def divisible_by_20(string):
    is_0 = False
    is_2_4_6_8_0 = False
    for i in string:
        if i == "0" and not is_0:
            is_0 = True
        elif i == "0" or i == "2" or i == "4" or i == "6" or i == "8":
            is_2_4_6_8_0 = True
    return is_0 and is_2_4_6_8_0

class Zad1:
    def __init__(self):
        self.number_of_data = 0
        self.table_with_data = []
        self.table_with_results = []
    def load_data(self):
        self.number_of_data = int(input())
        for i in range(self.number_of_data):
            self.table_with_data.append((input()))
    def fill_result(self):
        for i in self.table_with_data:
            if divisible_by_3(i) and divisible_by_20(i):
                self.table_with_results.append("red")
            else:
                self.table_with_results.append("cyan")
    def print_result(self):
        for i in self.table_with_results[:-1]:
            print(i)
        print(self.table_with_results[-1],end="")
    def run(self):
        self.load_data()
        self.fill_result()
        self.print_result()

zad1 = Zad1()
zad1.run()