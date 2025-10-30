import heapq

def bfs(board, start_pos, final_positions):
    queue = []

    stan = (start_pos, 0)
    queue.append(stan)
    visited = set()
    visited.add(tuple(start_pos))
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while len(queue) > 0:
        actual_stan = queue.pop(0)
        if actual_stan[0] in final_positions:
            return actual_stan[1]
        for move in moves:
            new_pos = (actual_stan[0][0] + move[0], actual_stan[0][1] + move[1])
            if board[new_pos[0]][new_pos[1]] != "#" and new_pos not in visited:
                queue.append((new_pos, actual_stan[1] + 1))
                visited.add(tuple(new_pos))


    return -1

def heuristics(actual_positions, final_positions, board):
    pom = -1
    for position in actual_positions:
        pom = max(pom, bfs(board, position, final_positions))
    return pom

def prepare_positions(positions):
    return tuple(sorted(positions))
class A:

    def __init__(self, komandos):
        self.komandos = komandos
        self.board = komandos.get_board()
        self.start_state = State(komandos.get_start_positions())
        self.queue = []
        # self.board_with_times = self.board
        # self.fill_board_with_times()
        heapq.heappush(self.queue ,((heuristics( self.start_state.get_pos(),
                                                 komandos.final_positions,komandos.get_board())),self.start_state))
        self.visited = set()
        self.on_queue = set()
        self.visited.add(self.start_state.get_pos())

    def is_final_state(self, state):
        return self.komandos.is_goal(state.get_pos())

    def fill_board_with_times(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != "#":
                    self.board_with_times[i][j] = bfs(self.board, (i, j), self.komandos.final_positions)

# przepełniona kolejka nie potrzebnie

    def add_children(self, state):
        for move in ['R', 'L', 'U', 'D']:
            new_positions = self.komandos.make_move(move, state.get_pos())
            new_positions = prepare_positions(new_positions)
            if new_positions not in self.visited:
                new_state = State(new_positions, state.get_moves() + move)
                h = heuristics( new_positions, self.komandos.final_positions,self.komandos.get_board())
                g = len(new_state.get_moves())
                f = g + h
                if len(new_positions) < len(state.get_pos()):
                    self.queue.clear()
                heapq.heappush(self.queue,(f, new_state))
                self.visited.add(new_positions)


    def solve(self):
        while len(self.queue) > 0:
            actual_state = self.queue.pop(0)[1]
            if self.is_final_state(actual_state):
                return actual_state
            self.add_children(actual_state)
        return None

class State:
    def __init__(self, actual_positions, moves: str = ""):
        self.actual_pos_list = actual_positions
        self.moves = moves

    def __lt__(self, other):
        return len(self.actual_pos_list) < len(self.actual_pos_list)

    def get_pos(self):
        return self.actual_pos_list

    def get_moves(self):
        return self.moves



class Komandos:
    def __init__(self):
        self.board = []
        self.read_board("zad_input.txt")
        pom = self.Find_S_and_B_positions()
        self.start_positions = prepare_positions(pom)
        self.start_moves = ""
        self.final_positions = self.find_G_and_B_positions()

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

    def find_G_and_B_positions(self):
        positions = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'G' or self.board[i][j] == 'B':
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


kom = Komandos()
A = A(kom)
state = A.solve()

with open("zad_output.txt", "w") as f:
    # Zapisujemy wynik do pliku
    f.write(state.get_moves())