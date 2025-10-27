class Zad2:
    def __init__(self):
        self.string = ""
        self.length = 0
        self.number_of_letter_in_result = ""

    def load_data(self):
        self.length = int(input())
        self.string = input()


    def fun(self):
        for i in range(self.length):
            if self.string[: i + 1] + self.string[: i + 1][:: -1] <= self.string[: (i+1) * 2]:
                return i
        return self.length - 1

    def calculate_and_print_result(self):
        self.number_of_letter_in_result = self.fun()
        pom = self.string[:self.number_of_letter_in_result + 1]
        pom = pom + pom[::-1]
        print(pom)


    def run(self):
        self.load_data()
        self.calculate_and_print_result()

iterator = int(input())
for i in range(iterator):
    zad2 = Zad2()
    zad2.run()