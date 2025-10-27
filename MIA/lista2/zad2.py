class Zad2:
    def __init__(self):
        self.reverse_cost = 0
        self.string = ""
        self.change_cost = 0
        self.length_of_string = 0
        self.result = 0
        self.number_of_ones = 0

    def load_data(self):
        tab = input().split()
        self.length_of_string = int(tab[0])
        self.reverse_cost = int(tab[1])
        self.change_cost = int(tab[2])
        self.string = input()

    def count_ones_blocks(self):
        if self.string[self.length_of_string -1] == "1":
            self.number_of_ones -= 1
        for i in range(1,self.length_of_string):
            if self.string[i] == "1" and self.string[i-1] == "0":
                self.number_of_ones += 1
    def fun(self):
        self.load_data()
        self.count_ones_blocks()
        if self.number_of_ones == -1:
            return 0
        if self.change_cost > self.reverse_cost:
            return self.number_of_ones * self.reverse_cost + self.change_cost
        else:
            return (self.number_of_ones + 1) * self.change_cost


zad2 = Zad2()
print(zad2.fun())
