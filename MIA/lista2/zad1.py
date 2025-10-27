
class Zad1:
    def __init__(self):
        self.number_of_athlete = 0
        self.number_of_programmers = 0
        self.length_of_string = 0
        self.string = ""
        self.name_of_student_to_place = ""

    def load_data(self):
        tab = input().split()
        self.length_of_string = int(tab[0])
        self.number_of_programmers = int(tab[1])
        self.number_of_athlete = int(tab[2])
        self.string = input()
        self.result = 0
        if self.number_of_athlete > self.number_of_programmers:
            self.name_of_student_to_place = "athlete"
        else:
            self.name_of_student_to_place= "programmer"

    def place_student(self,student):
        if student == "programmer":
            if self.number_of_programmers >0:
                self.result += 1
                self.number_of_programmers -=1
            self.name_of_student_to_place = "athlete"

        elif student == "athlete":
            if self.number_of_athlete > 0:
                self.number_of_athlete -=1
                self.result += 1
            self.name_of_student_to_place = "programmer"

        else:
            if self.number_of_athlete > self.number_of_programmers:
                self.name_of_student_to_place = "athlete"
            else:
                self.name_of_student_to_place = "programmer"



    def fun(self):
        self.load_data()
        for i in self.string:
            if i ==".":
                self.place_student(self.name_of_student_to_place)
            else:
                self.place_student("#")
        return self.result

zad1 = Zad1()
print(zad1.fun())