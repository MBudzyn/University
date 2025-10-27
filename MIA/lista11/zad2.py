
def sum_of_table(table):
    result = 0
    for element in table:
        result += element
    return result
class Zad2:
    def __init__(self):
        self.number_of_index_pairs = 0
        self.result = 0
        self.table_with_data = []
        self.table_with_index_pairs = []
        self.len_of_table_with_data = 0
        self.pom_table_index_count = [0]



    def load_data(self):
        self.len_of_table_with_data,self.number_of_index_pairs = map(int,input().split())
        self.table_with_data = list(map(int,input().split()))
        for i in range(self.number_of_index_pairs):
            self.table_with_index_pairs.append(list(map(int,input().split())))
        self.pom_table_index_count = self.pom_table_index_count * self.len_of_table_with_data

    def print_result(self):
        print(self.result)


    def count_index(self):
        pom_table = [0] * self.len_of_table_with_data
        print(pom_table)
        self.table_with_index_pairs.sort()
        for x,y in self.table_with_index_pairs:
            pom_table[x-1] += 1
        for i in range(self.len_of_table_with_data):
            for j in range(pom_table[i]):
                pass # TODO







    def fun(self):
        self.count_index()
        self.table_with_data.sort(reverse=True)
        self.pom_table_index_count.sort(reverse=True)
        for i in range(self.len_of_table_with_data):
            self.result += self.table_with_data[i] * self.pom_table_index_count[i]


    def run(self):

        self.load_data()
        self.fun()
        self.print_result()




zad2 = Zad2()
zad2.run()
