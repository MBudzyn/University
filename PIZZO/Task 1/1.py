# IDEA
# We need to store possible states of the automat in a ???(TODO)
# if the queue is empty, and the string is not empty, we need to return False
# if the string is empty, we need to check if any of the states is final
# if the string is not empty, for every possible state in the queue,
# and actual character in the string, we need to check if the transition is possible
# if it is, we need to add the new state to the new queue and remove the old state from the old queue
# at the end, we need to swap the queues and repeat the process

# NEED TO IMPLEMENT THE AUTOMAT
# we need to store the initial state, set of final states, and the transition function
# we need to implement the actual possible states of the automat as a set of states
# we need to implement the transition function as two dictionaries, one for the start_states (keys)
# and set of possible transitions (values), and one for the start_states-transitions (keys)
# and the resulting states (values)

# NEEDED METHODS FOR THE AUTOMAT CLASS
# 1) Load and transform data from Jason file
# 2) getters and setters for the automat attributes
# 3) Check if the string is accepted by the automat (main method)

# CORRECTIONS AND FINAL APPROACH
# I misunderstood the task, we need to implement the automat as a deterministic finite automat,
# so we only need to store the actual state of the automat (at the beginning it is the initial state)
# and the function that maps the actual state and the actual character to the next state

import json


class Automat:
    def __init__(self):
        self.actual_state = None
        self.accepting_states = None
        self.lines = None
        self.data = None
        self.moves = None
        self.load_file_from_input()
        self.load_automat(self.read_automat_path())
        self.transform_data()

    def load_automat(self, file_directory):
        with open(file_directory, 'r') as file:
            self.data = json.load(file)

    def read_automat_path(self):
        return self.lines.readline().strip()

    def load_file_from_input(self):
        fp = input().strip()
        self.lines = open(fp, "r")

    def transform_data(self):
        self.actual_state = self.data["initial"]
        self.accepting_states = set(self.data["accepting"])
        self.moves = {}
        for transition in self.data["transitions"]:
            self.moves[(transition["from"], transition["letter"])] = transition["to"]

    def run(self):
        while True:
            letter = self.lines.read(1)
            if letter == '\n':
                if self.actual_state in self.accepting_states:
                    print("yes")
                else:
                    print("no")
                self.actual_state = self.data["initial"]
            else:
                self.actual_state = self.moves.get((self.actual_state, letter), None)
                if self.actual_state is None:
                    return False

    def print_data(self):
        print(self.data["accepting"])
        print(self.data["alphabet"])
        print(self.data["states"])
        print(self.data["initial"])

        for transition in self.data["transitions"]:
            print("start state: ", transition["from"],
                  "move: ", transition["letter"],
                  "end state: ", transition["to"])
            
        print(self.moves)


aut = Automat()
aut.run()









