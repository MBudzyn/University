class Zad1:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.result = ""

    def load_data(self):
        self.a, self.b, self.c = map(int,input().split())


    def fun(self):
        first = self.a + self.c // 2
        second = self.b + self.c // 2
        if self.c % 2 == 1:
            first += 1
        if first > second:
            self.result = "First"
        else:
            self.result = "Second"
    def print_result(self):
        print(self.result)

    def run(self):
        self.load_data()
        self.fun()
        self.print_result()

iterator = int(input())
for i in range(iterator):
    zad1 = Zad1()
    zad1.run()
