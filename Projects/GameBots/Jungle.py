from typing import *
import sys
import random
import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import time

class Field:
    def __init__(self, type, animal = None):
        self.type = type
        self.animal = animal

    def __str__(self):
        return self.animal if self.animal is not None else self.type

    def __copy__(self):
        return Field(self.type, self.animal)

    def is_empty(self):
        return self.animal is None

    def animal_strength(self, animal):
        dict1 = {"R": 1, "C": 2, "D": 3, "W": 4, "J": 5, "T": 6, "L": 7, "E": 8}
        dict2 = {"r": 1, "c": 2, "d": 3, "w": 4, "j": 5, "t": 6, "l": 7, "e": 8}
        if animal in "rcdwjtle":
            return dict2[animal]
        else:
            return dict1[animal]
    def same_player_animal(self, animal2):
        if self.animal in "rcdwjtle" and animal2 in "rcdwjtle":
            return True
        elif self.animal in "RCDWJTLE" and animal2 in "RCDWJTLE":
            return True
        else:
            return False

    def can_be_placed(self, animal):
        if self.is_empty():
            if self.type == "~":
                if animal == "R" or animal == "r": # skrót do jednego ifa
                    return True
                else:
                    return False
            elif self.type == "**":
                if animal in "ewjrcdtl":
                    return False
                else:
                    return True
            elif self.type == "*":
                if animal in "EWJRCTDL":
                    return False
                else:
                    return True
            else:
                return True
        else:
            if self.same_player_animal(animal):
                return False
            elif self.type == "#":
                return True
            else:
                if self.animal in "Ee" and animal in "Rr":
                    return True
                elif self.animal in "Rr" and animal in "Ee": # tak sformułowane zasady uwzględniają bicie z wody przez szczura
                    return False
                else:
                    return self.animal_strength(animal) >= self.animal_strength(self.animal)










class Jungle:
    def __init__(self):
        self.board = self.initial_board()
        self.player_big_figures = {"L": (0,0), "T": (0, 6), "C": (1, 5), "D": (1, 1),
                           "E": (2, 6), "J": (2, 2), "R": (2, 0), "W": (2, 4)}
        self.player_small_figures = {"l": (8, 6), "t": (8, 0), "c": (7, 1), "d": (7, 5),
                           "e": (6, 0), "j": (6, 4), "r": (6, 6), "w": (6, 2)}
        self.animal_strength = {"R": 1, "C": 2, "D": 3, "W": 4, "J": 5, "T": 6, "L": 7, "E": 8} # przetłumaczenie na słownik bicia
        self.visited = set()

    def get_parsed_position(self):
        current_positions = tuple(
            sorted(list(self.player_big_figures.values()) + list(self.player_small_figures.values())))
        return current_positions

    def __copy__(self):
        new_board = Jungle()
        new_board.player_big_figures = self.player_big_figures.copy()
        new_board.player_small_figures = self.player_small_figures.copy()
        new_board.board = [[self.board[i][j].__copy__() for j in range(7)] for i in range(9)]
        new_board.visited = set(self.visited)
        new_board.animal_strength = self.animal_strength.copy()
        return new_board

    def test_coordinates(self):
        for i in self.player_big_figures:
            print(i, self.player_big_figures[i] ,self.board[self.player_big_figures[i][0]][self.player_big_figures[i][1]].animal)
        for i in self.player_small_figures:
            print(i, self.player_small_figures[i] ,self.board[self.player_small_figures[i][0]][self.player_small_figures[i][1]].animal)

    def is_player_small_animal(self, animal):
        return animal in "rcdwjtle"

    def is_legal_point(self, point):
        return 0 <= point[0] <= 8 and 0 <= point[1] <= 6

    def neighbour_fields(self, animal):
        p = []
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        if self.is_player_small_animal(animal):
            point = self.player_small_figures[animal]
        else:
            point = self.player_big_figures[animal]
        if animal in "cdwjer" or animal in "CDWJER":
            t = filter(lambda x: self.is_legal_point(x), [(point[0] + i, point[1] + j) for i, j in dir])
            return list(t)
        else:
            for direction in dir:
                new_point = (point[0] + direction[0], point[1] + direction[1])
                while self.is_legal_point(new_point) and self.board[new_point[0]][new_point[1]].type == "~":
                    if not self.board[new_point[0]][new_point[1]].is_empty():
                        new_point = (-3,-3)
                    new_point = (new_point[0] + direction[0], new_point[1] + direction[1])
                if self.is_legal_point(new_point):
                    p.append(new_point)
            return p

    def possible_moves(self, animal):
        p = []
        for i in self.neighbour_fields(animal):
            if self.board[i[0]][i[1]].can_be_placed(animal):
                if self.is_player_small_animal(animal):
                    p.append((self.player_small_figures[animal], i))
                else:
                    p.append((self.player_big_figures[animal], i))
        return p

    def all_small_possible_moves(self):
        p = []
        for animal in "recdwjtle":
            p += self.possible_moves(animal)
        return p

    def random_move(self, player):
        possible_moves = self.all_small_possible_moves() if player == 0 else self.all_big_possible_moves()
        return random.choice(possible_moves)

    def apply_move(self, move):
        if move not in self.all_small_possible_moves() and move not in self.all_big_possible_moves():
            sys.stderr.write("Illegal move")
        start, end = move
        start_field: Field = self.board[start[0]][start[1]]
        end_field: Field = self.board[end[0]][end[1]]
        if start_field.animal in "rcdwjtle":
            if end_field.is_empty():
                self.player_small_figures[start_field.animal] = end
                end_field.animal = start_field.animal
                start_field.animal = None
            else:
                attacked_animal = end_field.animal
                self.player_big_figures[attacked_animal] = (-3, -3)
                self.player_small_figures[start_field.animal] = end
                end_field.animal = start_field.animal
                start_field.animal = None
        else:
            if end_field.is_empty():
                self.player_big_figures[start_field.animal] = end
                end_field.animal = start_field.animal
                start_field.animal = None
            else:
                attacked_animal = end_field.animal
                self.player_small_figures[attacked_animal] = (-3, -3)
                self.player_big_figures[start_field.animal] = end
                end_field.animal = start_field.animal
                start_field.animal = None

    def alphabeta(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.is_terminal():
            # Tutaj możesz zastosować własną funkcję heurystyczną
            return self.h(), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.all_big_possible_moves():
                jungle_copy = self.__copy__()
                jungle_copy.apply_move(move)
                eval, _ = jungle_copy.alphabeta(depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.all_small_possible_moves():
                jungle_copy = self.__copy__()
                jungle_copy.apply_move(move)
                eval, _ = jungle_copy.alphabeta(depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def alphabeta_move(self, depth):
        _, best_move = self.alphabeta(depth, float('-inf'), float('inf'), True)
        return best_move

    def all_big_possible_moves(self):
        p = []
        for animal in "RCDWJETL":
            p += self.possible_moves(animal)
        return p

    def return_winner(self):
        if not self.is_terminal():
            return None
        if not self.board[0][3].is_empty():
            return 0
        else:
            return 1

    def is_terminal(self):
        return (not self.board[0][3].is_empty()) or (not self.board[8][3].is_empty())

    def play_random_game(self, starting_player):
        # 0 - small, 1 - big
        curr_player = starting_player

        while not self.is_terminal():
            if curr_player == 0:
                rmoves = self.all_small_possible_moves()
                if rmoves:
                    move = random.choice(rmoves)
                    #self.draw()
                    #print("state after move: ", move)
                    self.apply_move(move)
                    #self.draw()
                if self.is_terminal():
                    break
            else:
                rmoves = self.all_big_possible_moves()
                if rmoves:
                    move = random.choice(rmoves)
                    #self.draw()
                    #print("state after move: ", move)
                    self.apply_move(move)
                    #self.draw()
            curr_player = 1 - curr_player

    def play_random_game2(self, starting_player):
        b = self.__copy__()
        b.play_random_game(starting_player)
        return b.return_winner()


    def test_neighbour_fields(self):
        for i in self.player_big_figures:
            print(i, self.neighbour_fields(i))
        for i in self.player_small_figures:
            print(i, self.neighbour_fields(i))

    def initial_board(self):
        R1 = [Field(".", "L"), Field("."), Field("#"), Field("*"), Field("#"),Field("."), Field(".", "T")]
        R2 = [Field("."), Field(".","D"), Field("."), Field("#"), Field("."), Field(".", "C"),Field(".")]
        R3 = [Field(".","R"), Field("."), Field(".","J"), Field("."),
              Field(".","W"), Field("."), Field(".","E")]
        R4 = [Field("."), Field("~"),Field("~"),Field("."), Field("~"),Field("~" ),Field(".")]
        R5 = [Field("."), Field("~"), Field("~"), Field("."), Field("~"), Field("~"), Field(".")]
        R6 = [Field("."), Field("~"), Field("~"), Field("."), Field("~"), Field("~"), Field(".")]
        R7 = [Field(".","e"), Field("."), Field(".","w"),
              Field("."), Field(".","j"), Field("."), Field(".","r")]
        R8 = [Field("."), Field(".","c"), Field("."), Field("#"), Field("."), Field(".","d"), Field(".")]
        R9 = [Field(".","t"), Field("."), Field("#"), Field("**"), Field("#"),Field("."), Field(".","l")]

        return [R1, R2, R3, R4, R5, R6, R7, R8, R9]

    def h(self):
        weight = 0.3
        if self.is_terminal():
            if self.board[0][3].is_empty():
                return float("inf")
            else:
                return float("-inf")
        ps = []
        pb = []
        for k ,v in self.player_small_figures.items():
            if self.is_legal_point(v):
                ps.append(v)
        for k ,v in self.player_big_figures.items():
            if self.is_legal_point(v):
                pb.append(v)

        distance_to_end_pb = map(lambda x: abs(x[0] - 8) + abs(x[1] - 3), pb)
        pbd = sum(list(distance_to_end_pb))

        ps = map(lambda x: self.animal_strength[self.board[x[0]][x[1]].animal.upper()], ps)
        pb = map(lambda x: self.animal_strength[self.board[x[0]][x[1]].animal.upper()], pb)
        return sum(pb) - sum(ps) - pbd * weight
    def draw(self):
        for i in range(9):
            res = []
            for j in range(7):
                if self.board[i][j].animal is None:
                    res.append(self.board[i][j].type)
                else:
                    res.append(self.board[i][j].animal)

            print (''.join(res) )
        print()

class RandomBot:
    def __init__(self, jungle):
        self.jungle = jungle

    def random_move(self, player):
        possible_moves = self.jungle.all_small_possible_moves() if player == 0 else self.jungle.all_big_possible_moves()
        return random.choice(possible_moves)


class JungleBot:
    def __init__(self, jungle):
        self.jungle = jungle

    def best_move(self, player):
        possible_moves = self.jungle.all_small_possible_moves() if player == 1 else self.jungle.all_big_possible_moves()
        best_move = None
        max_wins = -1

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.simulate_games, move, player) for move in possible_moves]

            # Pobranie wyników zakończonych wątków
            for future in futures:
                wins = future.result()[0]
                move = future.result()[1] # Pobranie ruchu z argumentów przyszłości
                if wins > max_wins:
                    best_move = move
                    max_wins = wins

        return best_move

    def simulate_games(self, move, player, num_games=4):
        wins = 0
        for _ in range(num_games):
            jungle_copy = self.jungle.__copy__()
            jungle_copy.apply_move(move)
            result = jungle_copy.play_random_game2(player)
            if result == player:
                wins += 1
        return wins, move

# Rozgrywka między botem a losowym botem
def play_gameJR():
    jungle = Jungle()
    jungle_copy = jungle.__copy__()

    player = 0  # Gracz o indeksie 0 zaczyna

    while not jungle_copy.is_terminal():
        if player == 0:
            bot = JungleBot(jungle_copy)
            move = bot.best_move(player)
        else:
            random_bot = RandomBot(jungle_copy)
            move = random_bot.random_move(player)

        jungle_copy.apply_move(move)
        jungle_copy.draw()
        print("Player", player, "moves:", move)

        player = 1 - player

    winner = jungle_copy.return_winner()
    if winner is None:
        print("Remis!")
    else:
        print("Wygrał gracz:", winner)

def play_games_ab():
        player = 0
        B = Jungle()

        while True:
            if player == 1:
                move = B.alphabeta_move(3)
                B.apply_move(move)
                print("alfabeta")
                B.draw()

            else:
                move = B.random_move(player)
                B.apply_move(move)
                print("random")
                B.draw()

            player = 1 - player
            if B.is_terminal():
                break

#alfa zawsze gra dużymi bot z zadania 3 małymi i w zależności kto zaczyna taka jest kolejność ruchów
def play_games_abVSJ(times=10):
    results = {"Bot 1 wins": 0, "Bot 2 wins": 0, "Draw": 0}
    for i in range(times):
        player = i%2
        B = Jungle()

        while True:
            if player == 0:
                move = B.alphabeta_move(3)
                B.apply_move(move)
                print("MiniMax")
                B.draw()
            else:
                # Tworzymy kopię stanu gry dla JungleBota
                B_copy = B.__copy__()
                bot = JungleBot(B_copy)
                move = bot.best_move(player)
                B.apply_move(move)
                print("JungleBot")
                B.draw()

            player = 1 - player

            if B.is_terminal():
                result = "Draw" if B.return_winner() == 0 else "Bot 1 wins" if B.return_winner() > 0 else "Bot 2 wins"
                results[result] += 1
                break
    print(results)


play_games_abVSJ()
