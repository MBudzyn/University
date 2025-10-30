
def min_cost_of_k_elements(table,k):
    result = 0
    pom_table = []
    for i in range(len(table)):
        pom_table.append(table[i] + (i + 1) * k)
    pom_table.sort()
    for i in range(k):
        result += pom_table[i]
    return result


class Zad1():
    def __init__(self):
        self.number_of_data = 0
        self.max_cost = 0
        self.table_with_data = []
        self.result = []
    def load_data(self):
        self.number_of_data,self.max_cost = map(int,(input().split()))
        self.table_with_data = list(map(int,input().split()))

    def fun(self):
        min_number_of_elements = 0
        max_number_of_elements = self.number_of_data
        while max_number_of_elements - min_number_of_elements >1:
            next_guess = (min_number_of_elements + max_number_of_elements)//2
            if min_cost_of_k_elements(self.table_with_data,next_guess) < self.max_cost:
                min_number_of_elements = next_guess
            else:
                max_number_of_elements = next_guess
        min_cost = min_cost_of_k_elements(self.table_with_data,min_number_of_elements)
        max_cost = min_cost_of_k_elements(self.table_with_data,max_number_of_elements)
        if min_cost_of_k_elements(self.table_with_data,max_number_of_elements) <= self.max_cost:
            self.result = [max_number_of_elements,max_cost]
        else:
            self.result = [min_number_of_elements,min_cost]
    def run(self):
        self.load_data()
        self.fun()
        self.print_result()
    def print_result(self):
        print(self.result[0],self.result[1])

zad1 = Zad1()
zad1.run()



