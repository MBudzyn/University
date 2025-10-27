class Zad2:
    def __init__(self):
        self.rows = 0
        self.letters = 0
        self.worlds_table = []


    def load_data(self):
        tmp_table = input().split()
        self.rows = int(tmp_table[0])
        self.letters = int(tmp_table[1])
        for i in range(self.rows):
            self.worlds_table.append(input())

    def fun(self):
        vika = "vika"
        iterator = 0
        for i in range(self.letters):
            for j in range(self.rows):
                if self.worlds_table[j][i] == vika[iterator]:
                    iterator+=1
                    if iterator == 4:
                        return "YES"
                    break
        return "NO"
def funkcja():
    count = int(input())
    for i in range(count):
        zad = Zad2()
        zad.load_data()
        print(zad.fun())
funkcja()