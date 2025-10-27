import math

def czy_sa_rownolegle_do_x(p1, p2):
    return p1[1] == p2[1]



def warunek_zadania(p1,p2, p3):
    if czy_sa_rownolegle_do_x(p1,p2) and p3[1] < p1[1]:
        return abs(p1[0] - p2[0])
    else: return 0

class Zad1:
    def __init__(self):
        self.list_of_coordinates = []
        self.result = 0

    def load_data(self):
        for _ in range(3):
            self.list_of_coordinates.append(list(map(int,input().split())))

    def fun(self):
        self.result += warunek_zadania(self.list_of_coordinates[0],self.list_of_coordinates[1],self.list_of_coordinates[2])
        self.result += warunek_zadania(self.list_of_coordinates[0],self.list_of_coordinates[2],self.list_of_coordinates[1])
        self.result += warunek_zadania(self.list_of_coordinates[1],self.list_of_coordinates[2],self.list_of_coordinates[0])




    def print_result(self):
        print(self.result)


    def run(self):
        self.load_data()
        self.fun()
        self.print_result()


iterator = int(input())
for _ in range(iterator):
    zad1 = Zad1()
    zad1.run()
