class Zad1:
    def __init__(self):
        self.given_string = ""
        self.result = 0
        self.all_substrings_int = []

    def number_of_substrings_divided_by_4(self):
        for i in self.all_substrings_int:
            if i%4 == 0:
                self.result +=1

    def substrings_only_two_last(self):
        multi = 0
        for i in range(1, len(self.given_string) + 1):
            multi +=1
            first = self.given_string[i - 1: i+ 1]
            second = self.given_string[i -1 : i]
            if int(second) % 4 == 0:
                self.result +=1
            if int(first) % 4 == 0:
                self.result += multi
        if int(self.given_string[-1:]) %4 == 0:
            self.result -= multi

    def load_data(self):
        self.given_string = input()


    def print_result(self):
        print(self.result)
    def run(self):
        self.load_data()
        self.substrings_only_two_last()
        #self.number_of_substrings_divided_by_4()
        self.print_result()

zad1 = Zad1()
zad1.run()



