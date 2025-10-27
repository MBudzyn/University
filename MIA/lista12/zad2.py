class Zad2:
    def __init__(self):
        self.table_with_stones = []
        self.number_of_stones = 0
        self.result = ""

    def load_data(self):
        self.number_of_stones = int(input())
        self.table_with_stones = list(map(int,input().split()))


    def fun(self):
        ones = 0
        for i in range(self.number_of_stones - 1):
            if self.table_with_stones[i] == 1:
                ones += 1
            else:
                break
        if ones % 2 == 1:
            self.result = "Second"
        else:
            self.result = "First"
    def print_result(self):
        print(self.result)

    def run(self):
        self.load_data()
        self.fun()
        self.print_result()

iterator = int(input())
for i in range(iterator):
    zad2 = Zad2()
    zad2.run()
