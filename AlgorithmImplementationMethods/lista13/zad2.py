class Zad2:
    def __init__(self):
        self.table_with_comends = []
        self.table_with_stones = []
        self.number_of_stones = 0
        self.number_of_comends = 0
        self.sorted_table_with_stones = []
        self.table_with_sums = []
        self.table_with_sorted_sums = []

    def load_data(self):
        self.number_of_stones = int(input())
        self.table_with_stones = list(map(int,input().split()))
        self.sorted_table_with_stones = sorted(self.table_with_stones)
        self.number_of_comends = int(input())
        for _ in range(self.number_of_comends):
            self.table_with_comends.append(list(map(int,input().split())))

    def fill_tables_with_sums(self):
        self.table_with_sums.append(self.table_with_stones[0])
        self.table_with_sorted_sums.append(self.sorted_table_with_stones[0])
        for i in range(1,self.number_of_stones):
            self.table_with_sums.append(self.table_with_sums[i - 1] + self.table_with_stones[i])
            self.table_with_sorted_sums.append(self.table_with_sorted_sums[i - 1] + self.sorted_table_with_stones[i])

    def execute_commend(self, commend):
        if commend[0] == 1:
            if commend[1] == 1:
                return self.table_with_sums[commend[2] - 1]
            else:
                return self.table_with_sums[commend[2] - 1] - self.table_with_sums[commend[1] - 2]
        else:
            if commend[1] == 1:
                return self.table_with_sorted_sums[commend[2] - 1]
            else:
                return self.table_with_sorted_sums[commend[2] - 1] - self.table_with_sorted_sums[commend[1] - 2]


    def print_result(self):
        for commend in self.table_with_comends:
            print(self.execute_commend(commend))

    def run(self):
        self.load_data()
        self.fill_tables_with_sums()
        self.print_result()


zad2 = Zad2()
zad2.run()

