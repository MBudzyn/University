import random
import time
import multiprocessing
class Board:
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def __init__(self, start_player):
        self.board = self.initial_board()
        self.fields = set()
        self.move_list = []
        self.history = []
        self.player_symbol = start_player
        self.opponent_symbol = 1 - start_player
        self.player_token = 2
        self.opponent_token = 2
        for i in range(8):
            for j in range(8):
                if self.board[i][j] is None:
                    self.fields.add((j, i))

    @staticmethod
    def initial_board():
        B = [[None] * 8 for _ in range(8)]
        B[3][3] = 1
        B[4][4] = 1
        B[3][4] = 0
        B[4][3] = 0
        return B

    def moves(self, player):
        res = []
        for (x, y) in self.fields:
            if any(self.can_beat(x, y, direction, player) for direction in Board.dirs):
                res.append((x, y))
        if not res:
            return [None]
        return res

    def can_beat(self, x, y, d, player):
        dx, dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x, y) == 1 - player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x, y) == player

    def get(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return self.board[y][x]
        return None

    def draw(self):
        for i in range(8):
            res = []
            for j in range(8):
                b = self.board[i][j]
                if b == None:
                    res.append('.')
                elif b == 1:
                    res.append('#')
                else:
                    res.append('o')
            print (''.join(res) )
        print()

    def do_move(self, move, player):
        self.history.append([x[:] for x in self.board])
        self.move_list.append(move)

        if move is None or (move[0] == -1 and move[1] == -1):
            return

        x, y = move
        x0, y0 = move
        self.board[y][x] = player
        if player == self.player_symbol:
            self.player_token += 1
        else:
            self.opponent_token += 1
        self.fields -= {(x, y)}
        for dx, dy in self.dirs:
            x, y = x0, y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x, y) == 1 - player:
                to_beat.append((x, y))
                x += dx
                y += dy
            if self.get(x, y) == player:
                for nx, ny in to_beat:
                    self.board[ny][nx] = player
                    if player == self.player_symbol:
                        self.player_token += 1
                        self.opponent_token -= 1
                    else:
                        self.opponent_token += 1
                        self.player_token -= 1


    def result2(self):
        res = 0
        for y in range(8):
            for x in range(8):
                b = self.board[y][x]
                if b == 0:
                    res += 1
                elif b == 1:
                    res -= 1
        return res


    def h(self):
        bonus = 0
        bonus += -10 if self.board[0][0] == 1 else 10 if self.board[0][0] == 0 else 0
        bonus += -10 if self.board[0][7] == 1 else 10 if self.board[0][7] == 0 else 0
        bonus += -10 if self.board[7][0] == 1 else 10 if self.board[7][0] == 0 else 0
        bonus += -10 if self.board[7][7] == 1 else 10 if self.board[7][7] == 0 else 0
        for i in range(1, 7):
            bonus += -4 if self.board[0][i] == 1 else 4 if self.board[0][i] == 0 else 0
            bonus += -4 if self.board[i][0] == 1 else 4 if self.board[i][0] == 0 else 0
            bonus += -4 if self.board[7][i] == 1 else 4 if self.board[7][i] == 0 else 0
            bonus += -4 if self.board[i][7] == 1 else 4 if self.board[i][7] == 0 else 0




        return (self.player_token - self.opponent_token) + bonus



    def result(self):
        return self.player_token - self.opponent_token


    def terminal(self):
        if not self.fields:
            return True
        if len(self.move_list) < 2:
            return False
        return self.move_list[-1] == self.move_list[-2] == None

    def random_move(self, player):
        ms = self.moves(player)
        if ms:
            return random.choice(ms)
        return [None]

    def alphabeta_move(self, player, depth, alpha=float("-inf"), beta=float("inf")):
        if depth == 0 or self.terminal():
            return self.h(), None

        best_value = float('-inf') if player == 0 else float('inf')
        best_move = None

        moves = self.moves(player)

        for move in moves:
            new_board = Board(player)
            new_board.board = [row[:] for row in self.board]
            new_board.fields = set(self.fields)
            new_board.move_list = list(self.move_list)
            new_board.history = list(self.history)
            new_board.player_token = self.player_token
            new_board.opponent_token = self.opponent_token
            new_board.do_move(move, player)

            value, _ = new_board.alphabeta_move(1 - player, depth - 1, alpha, beta)

            if player == 0:
                if value > best_value:
                    best_value = value
                    best_move = move
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            else:
                if value < best_value:
                    best_value = value
                    best_move = move
                beta = min(beta, best_value)
                if beta <= alpha:
                    break

        return best_value, best_move

import sys

def get_communication():
    while True:
        try:
            line = input().strip()  # Odczytaj linijkę ze standardowego wejścia
            parts = line.split()  # Podziel linijkę na części

            # Sprawdź typ komunikatu i zwróć odpowiednie wartości
            if parts[0] == 'UGO':
                time_for_move = float(parts[1])
                remaining_time = float(parts[2])
                return 'UGO', time_for_move, remaining_time
            elif parts[0] == 'HEDID':
                time_for_move = float(parts[1])
                remaining_time = float(parts[2])
                move_info = [int(x) for x in parts[3:]]  # Parsowanie informacji o ruchu
                return 'HEDID', time_for_move, remaining_time, move_info
            elif line == 'ONEMORE':
                return 'ONEMORE',
            elif line == 'BYE':
                return 'BYE',
            else:
                # Nieznany komunikat
                print("Nieznany komunikat:", line, file=sys.stderr)
        except EOFError:
            # Zakończ pętlę gdy koniec pliku wejściowego
            break

# Przykład użycia funkcji get_communication()
class Player(object):
    def __init__(self):
        self.game = None
        self.my_player = None
        self.reset()

    def reset(self):
        self.say('RDY')

    def say(self, what):
        sys.stdout.write(what)
        sys.stdout.write('\n')
        sys.stdout.flush()

    def hear(self):
        line = sys.stdin.readline().strip()
        return line.split()

    def loop(self):
        CORNERS = {(0, 0), (0, 7), (7, 0), (7, 7)}
        while True:
            cmd, args = self.hear()
            if cmd == 'HEDID':
                if self.my_player is None:
                    # Ustalamy, czy rozpoczynamy grę czy dołączamy do gry
                    unused_move_timeout, unused_game_timeout = map(float, args[:2])
                    self.my_player = 1 - int(args[2])  # Kolor gracza, który wykonał ruch
                    self.game = Board(self.my_player)
                else:
                    unused_move_timeout, unused_game_timeout = map(float, args[:2])
                    move = tuple((int(m) for m in args[2:]))
                    if move == (-1, -1):
                        move = None
                    self.game.do_move(move, 1 - self.my_player)
            elif cmd == 'ONEMORE':
                self.reset()
                continue
            elif cmd == 'BYE':
                break
            else:
                assert cmd == 'UGO'
                assert not self.game.move_list
                self.my_player = 0
                self.game = Board(self.my_player)

            moves = self.game.moves(self.my_player)
            better_moves = list(set(moves) & CORNERS)

            if better_moves:
                move = random.choice(better_moves)
                self.game.do_move(move, self.my_player)
            elif moves:
                move = random.choice(moves)
                self.game.do_move(move, self.my_player)
            else:
                self.game.do_move(None, self.my_player)
                move = (-1, -1)
            self.say('IDO %d %d' % move)


if __name__ == '__main__':
    player = Player()
    player.loop()