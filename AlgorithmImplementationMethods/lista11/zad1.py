class Zad1:
    def __init__(self):
        self.number_of_data = 0
        self.result = 0
        self.table_with_data = []
        self.pom_table = [0]



    def load_data(self):
        self.number_of_data = int(input())
        self.table_with_data = list(map(int,input().split()))
        self.pom_table = self.pom_table * self.number_of_data

    def fun(self):
        index = 0
        for element in self.table_with_data:
            self.pom_table[self.number_of_data - element] = element
            while index < self.number_of_data and self.pom_table[index] != 0:
                print(self.pom_table[index], end=" ")
                index += 1
            print()

    def run(self):
        self.load_data()
        self.fun()



zad1 = Zad1()
zad1.run()
