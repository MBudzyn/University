from automata.fa.dfa import DFA
class Automat:
    def __init__(self):
        self.accepting_states = set()
        self.transitions = {}
        self.alfabet = set()
        self.states = set()
        self.states.add("q0")
        self.initial_state = "q0"
        self.not_accepting_states = set()
        self.words = []

    def load_data(self):
        first_line = input().strip()
        num_words, automat_size = map(int, first_line.split())
        for _ in range(num_words):
            self.words.append(input().strip())

    def word_path(self, word):
        is_accepting = True if word[0] == "+" else False
        word = word[1:]
        actual_state = self.initial_state
        for letter in word:
            if letter not in self.alfabet:
                self.alfabet.add(letter)

            if actual_state not in self.transitions:
                self.transitions[actual_state] = {}

            if letter not in self.transitions[actual_state]:
                new_state = "q" + str(len(self.states))
                self.transitions[actual_state][letter] = new_state
                self.states.add(new_state)

            actual_state = self.transitions[actual_state][letter]

        if is_accepting:
            self.accepting_states.add(actual_state)
        else:
            self.not_accepting_states.add(actual_state)

    def hopcroft_minimization(self):
        partitions = [self.accepting_states, self.not_accepting_states]
        worklist = [self.accepting_states, self.not_accepting_states]
        while worklist:
            current_partition = worklist.pop()

            for letter in self.alfabet:
                involved_states = {state for state in self.states if
                                   self.transitions.get(state, {}).get(letter) in current_partition}

                new_partitions = []
                for partition in partitions:
                    intersection = partition.intersection(involved_states)
                    difference = partition.difference(involved_states)

                    if intersection and difference:
                        partitions.remove(partition)
                        partitions.append(intersection)
                        partitions.append(difference)

                        if partition in worklist:
                            worklist.remove(partition)
                            worklist.append(intersection)
                            worklist.append(difference)
                        else:
                            worklist.append(intersection if len(intersection) < len(difference) else difference)

        minimized_transitions = {}
        state_mapping = {}

        for i, partition in enumerate(partitions):
            new_state = f"q{i}"
            for state in partition:
                state_mapping[state] = new_state
                print(new_state)

        for state in self.transitions:
            new_state = state_mapping[state]
            if new_state not in minimized_transitions:
                minimized_transitions[new_state] = {}
            for letter, target in self.transitions[state].items():
                minimized_transitions[new_state][letter] = state_mapping[target]

        self.states = set(state_mapping.values())
        self.transitions = minimized_transitions
        self.accepting_states = {state_mapping[state] for state in self.accepting_states}
        self.initial_state = state_mapping[self.initial_state]

    def create_trie(self):
        for word in self.words:
            self.word_path(word)

    def add_trap_state(self):
        trap_state = "q" + str(len(self.states))
        self.states.add(trap_state)
        for state in self.states:
            for letter in self.alfabet:
                if state not in self.transitions:
                    self.transitions[state] = {}
                if letter not in self.transitions[state]:
                    self.transitions[state][letter] = trap_state

    def print_automat(self):
        transitions = []
        for transition in self.transitions:
            for letter in self.transitions[transition]:
                transitions.append({"letter" : letter,
                                    "from" : transition,
                                    "to:" : self.transitions[transition][letter]})
        to_print = {
            "alphabet": list(self.alfabet),
            "states": list(self.states),
            "initial": self.initial_state,
            "accepting": list(self.accepting_states),
            "transitions": transitions

        }
        print(to_print)


automat = Automat()
automat.load_data()
automat.create_trie()
automat.add_trap_state()
automat.hopcroft_minimization()
automat.print_automat()

dfa = DFA(
    states=automat.states,
    input_symbols=automat.alfabet,
    transitions=automat.transitions,
    initial_state=automat.initial_state,
    final_states=automat.accepting_states
)

dfa = dfa.minify()
automat.states = dfa.states
automat.transitions = dfa.transitions
automat.initial_state = dfa.initial_state
automat.accepting_states = dfa.final_states
automat.print_automat()

