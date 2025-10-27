
class Zad1:
    def __init__(self):
        self.cube1 = []
        self.cube2 = []
        self.cube3 = []
        self.number_of_dice = 0
        self.res = []

    def load_data(self):
        self.number_of_dice = int(input())

        for i in range(self.number_of_dice):
            if i == 0:
                self.cube1 = input().split(" ")
            if i == 1:
                self.cube2 = input().split(" ")
            if i == 2:
                self.cube3 = input().split(" ")

    def permutation_3(self):

        for i in range(6):
            for j in range(6):
                self.res.append(int(self.cube1[i] + self.cube2[j]))
                self.res.append(int(self.cube1[i] + self.cube3[j]))
                self.res.append(int(self.cube2[i] + self.cube3[j]))
                self.res.append(int(self.cube2[i] + self.cube1[j]))
                self.res.append(int(self.cube3[i] + self.cube2[j]))
                self.res.append(int(self.cube3[i] + self.cube1[j]))

        for i in range(6):
            self.res.append(int(self.cube1[i]))
            self.res.append(int(self.cube2[i]))
            self.res.append(int(self.cube3[i]))

        self.res = list(set(self.res))

    def permutation_2(self):
        for i in range(6):
            for j in range(6):
                self.res.append(int(self.cube1[i] + self.cube2[j]))
                self.res.append(int(self.cube2[i] + self.cube1[j]))

        for i in range(6):
            self.res.append(int(self.cube1[i]))
            self.res.append(int(self.cube2[i]))

        self.res = list(set(self.res))
    def permutation_1(self):
        for i in range(6):
            self.res.append(int(self.cube1[i]))
        self.res = list(set(self.res))

    def function(self):
        if self.number_of_dice == 3:
            self.permutation_3()
        if self.number_of_dice == 2:
            self.permutation_2()
        if self.number_of_dice == 1:
            self.permutation_1()

        self.res.sort()
        if self.res[0] == 0:
            self.res = self.res[1:]
        for i in range(1,len(self.res) + 1):
            if self.res[i-1] != i:
                return i-1
        return len(self.res)

def cubes_for_masha():
    zad1 = Zad1()
    zad1.load_data()
    return zad1.function()



print(cubes_for_masha())

