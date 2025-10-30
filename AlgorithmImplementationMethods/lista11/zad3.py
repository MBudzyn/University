class Zad3:
    def __init__(self):
        self.number_of_dominos = 0
        self.table_with_dominos = []
        self.result_pom_table = []

    def load_data(self):
        self.number_of_dominos = int(input())
        for i in range(self.number_of_dominos):
            pom = list(map(int,input().split(" ")))
            pom.append(i)
            self.table_with_dominos.append(pom)
        self.table_with_dominos.sort(reverse = True)

    def fun(self):
        pom_list = [self.table_with_dominos[0][2], 1]
        self.result_pom_table.append(pom_list)
        for i in range(1, self.number_of_dominos):
            if self.table_with_dominos[i][0] + self.table_with_dominos[i][1] >= self.table_with_dominos[i-1][0]:
                pom_list = [self.table_with_dominos[i][2], self.result_pom_table[i - 1][1] + 1]
            else:
                pom_list = [self.table_with_dominos[i][2], 1]
            self.result_pom_table.append(pom_list)

    def print_table(self):
        print(self.result_pom_table)

    def run(self):
        self.load_data()
        self.fun()
        self.print_table()



zad3 = Zad3()
zad3.run()