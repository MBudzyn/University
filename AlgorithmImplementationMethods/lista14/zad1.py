import math

def task_condition(argument):
    if argument < 0:
        return True
    sqr = math.sqrt(argument)
    if sqr == int(sqr):
        return False
    else:
        return True
class Zad1:
    def __init__(self):
        self.original_string = ""
        self.received_string = ""
        self.result = 0.0
        self.expected_sum = 0
        self.number_of_question_marks = 0

    def calculate_expected_sum(self):
        for _char in self.original_string:
            if _char == "+":
                self.expected_sum += 1
            else:
                self.expected_sum -= 1
        for _char in self.received_string:
            if _char == "+":
                self.expected_sum -= 1
            elif _char == "-":
                self.expected_sum += 1
        self.expected_sum = self.expected_sum * -1


    def count_question_marks(self):
        for _char in self.received_string:
            if _char == "?":
                self.number_of_question_marks += 1

    def calculate_probabilitie(self):
        if self.number_of_question_marks == 0 and self.expected_sum == 0:
            self.result = 1
        elif abs(self.expected_sum) > self.number_of_question_marks:
            self.result = 0
        else:
            all_possibilities = 2 ** self.number_of_question_marks
            number_of_same_symbols = (self.number_of_question_marks - abs(self.expected_sum)) / 2
            if number_of_same_symbols != int(number_of_same_symbols):
                self.result = 0
            else:
                number_of_pluses = number_of_same_symbols + abs(self.expected_sum)
                correct_strings = math.comb(self.number_of_question_marks, int(number_of_pluses))
                self.result = correct_strings / all_possibilities

    def load_data(self):
        self.original_string = input()
        self.received_string = input()

    def fun(self):
        self.count_question_marks()
        self.calculate_expected_sum()
        self.calculate_probabilitie()



    def print_result(self):
        print(self.result)

    def run(self):
        self.load_data()
        self.fun()
        self.print_result()
zad1 = Zad1()
zad1.run()
