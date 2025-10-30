from random import *

def prepare_positions(positions):
    return tuple(sorted(positions))


class BFS:

    def __init__(self, komandos):
        self.komandos = komandos
        self.board = komandos.get_board()
        self.start_state = State(komandos.get_start_positions(), komandos.start_moves)
        self.queue = [self.start_state]
        self.visited = set()
        self.visited.add(self.start_state.get_pos())

    def is_final_state(self, state):
        return self.komandos.is_goal(state.get_pos())

    def add_children(self, state):
        for move in ['R', 'L', 'U', 'D']:
            new_positions = self.komandos.make_move(move, state.get_pos())
            new_positions = prepare_positions(new_positions)
            new_state = State(new_positions, state.get_moves() + move)
            if new_positions not in self.visited:
                self.queue.append(new_state)
                self.visited.add(new_positions)

    def solve(self):
        while len(self.queue) > 0:
            actual_state = self.queue.pop(0)
            if self.is_final_state(actual_state):
                return actual_state
            self.add_children(actual_state)
        return None


class State:
    def __init__(self, actual_positions, moves: str = ""):
        self.actual_pos_list = actual_positions
        self.moves = moves

    def get_pos(self):
        return self.actual_pos_list

    def get_moves(self):
        return self.moves


class Komandos:
    def __init__(self):
        self.board = []
        self.read_board("zad_input.txt")
        self.start_positions = self.Find_S_and_B_positions()
        str, pom = self.random_moves(11)
        self.start_positions = prepare_positions(pom)
        self.start_moves = str


    def get_board(self):
        return self.board

    def get_start_positions(self):
        return self.start_positions

    def read_board(self, input_file):
        with open(input_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                self.board.append(list(line.strip()))

    def print_board(self):
        for row in self.board:
            print(''.join(row))

    def Find_S_and_B_positions(self):
        positions = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'S' or self.board[i][j] == 'B':
                    positions.append((i, j))
        return positions

    def move_right(self, actual_positions):
        new_positions = []
        for position in actual_positions:
            if self.board[position[0]][position[1] + 1] != "#":
                new_pos = (position[0], position[1] + 1)
            else:
                new_pos = position
            new_positions.append(new_pos)
        return new_positions

    def move_left(self, actual_positions):
        new_positions = []
        for position in actual_positions:
            if self.board[position[0]][position[1] - 1] != "#":
                new_pos = (position[0], position[1] - 1)
            else:
                new_pos = position
            new_positions.append(new_pos)
        return new_positions

    def move_up(self, actual_positions):
        new_positions = []
        for position in actual_positions:
            if self.board[position[0] - 1][position[1]] != "#":
                new_pos = (position[0] - 1, position[1])
            else:
                new_pos = position
            new_positions.append(new_pos)
        return new_positions

    def move_down(self, actual_positions):
        new_positions = []
        for position in actual_positions:
            if self.board[position[0] + 1][position[1]] != "#":
                new_pos = (position[0] + 1, position[1])
            else:
                new_pos = position
            new_positions.append(new_pos)
        return new_positions

    def make_move(self, move, actual_positions):
        new_positions = []
        if move == 'R':
            new_positions = self.move_right(actual_positions)
        elif move == 'L':
            new_positions = self.move_left(actual_positions)
        elif move == 'D':
            new_positions = self.move_down(actual_positions)
        elif move == 'U':
            new_positions = self.move_up(actual_positions)
        return new_positions

    def print_all_B_G_pos(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'B' or self.board[i][j] == 'G':
                    print(i, j)

    def is_goal(self, actual_positions):
        for position in actual_positions:
            if self.board[position[0]][position[1]] != 'B' \
                    and self.board[position[0]][position[1]] != 'G':
                return False
        return True

    def random_moves(self, iterations):
        string = ""
        moves = ['R', 'U', 'L', 'D']
        kom_positions = self.get_start_positions()
        last_ind = -1
        zakres  = 10


        for _ in range(iterations):
            index = randint(0, 3)
            while index == last_ind  or index == (last_ind + 2) % 4:
                index = randint(0, 3)
            for i in range(zakres):
                kom_positions = self.make_move(moves[index], kom_positions)
                kom_positions = set(kom_positions)
                kom_positions = tuple(kom_positions)
                string += moves[index]
            last_ind = index

            if len(kom_positions) <= 2:
                break


        print(len(kom_positions))
        return string, kom_positions

kom = Komandos()

# Tworzymy instancję klasy BFS i rozwiązujemy problem
bfs = BFS(kom)
state = bfs.solve()

# Zapisujemy wynik do pliku
with open("zad_output.txt", "w") as f:
    f.write(state.get_moves())