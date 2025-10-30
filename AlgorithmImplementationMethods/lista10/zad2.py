class Zad1:
    def __init__(self):
        self.word_s = ""
        self.word_t = ""
        self.result = ""
        self.dict_s = {}
        self.dict_t = {}

    def load_data(self):
        self.word_s = input()
        self.word_t = input()

    def fill_dicts(self):
        for i in self.word_s:
            if i in self.dict_s:
                self.dict_s[i] += 1
            else:
                self.dict_s[i] = 1

        for i in self.word_t:
            if i in self.dict_t:
                self.dict_t[i] += 1
            else:
                self.dict_t[i] = 1

    def is_t_less_than_s(self):
        for key in self.dict_t:
            if key not in self.dict_s:
                return False
            elif self.dict_t[key] > self.dict_s[key]:
                return False
        return True

    def has_t_and_s_same_length(self):
        return len(self.word_t) == len(self.word_s)

    def only_deleting_letters(self):
        word_s = self.word_s
        word_t = self.word_t

        for letter in word_s:
            if letter == word_t[0]:
                word_t = word_t[1:]
                if word_t == "":
                    return True
        return False

    def print_result(self):
        print(self.result)


    def fun(self):
        if not self.is_t_less_than_s():
            self.result = "need tree"
        elif self.has_t_and_s_same_length():
            self.result = "array"
        elif self.only_deleting_letters():
            self.result = "automaton"
        else:
            self.result = "both"


    def run(self):
        self.load_data()
        self.fill_dicts()
        self.fun()
        self.print_result()

zad1 = Zad1()
zad1.run()
