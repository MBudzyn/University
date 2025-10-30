class Zad3:
    def __init__(self):
        self.table_with_pairs = []
        self.result = ""



    def load_data(self):
        number_of_pairs = int(input())
        for i in range(number_of_pairs):
            self.table_with_pairs.append(list(map(int,input().split(" "))))






    def fun(self):
        number_of_odd_rows = 0
        for x,y in self.table_with_pairs:
            if x % 2 == 0:
                pom = y//2
                if pom % 2 ==1:
                    number_of_odd_rows += 1
            else:
                pom = (y+1)//2
                if pom % 2 == 1:
                    number_of_odd_rows +=1
        if number_of_odd_rows % 2 == 0:
            self.result = "bolik"
        else:
            self.result = "tolik"


    def print_result(self):
        print(self.result)
    def run(self):
        self.load_data()
        self.fun()
        self.print_result()

zad3 = Zad3()
zad3.run()