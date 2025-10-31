import random
import time
import multiprocessing
class Board:
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def __init__(self):
        self.board = self.initial_board()
        self.fields = set()
        self.move_list = []
        self.history = []
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

        if move is None:
            return
        x, y = move
        x0, y0 = move
        self.board[y][x] = player
        if player == 0:
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
                    if player == 0:
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
        bonus += -7 if self.board[0][0] == 1 else 7 if self.board[0][0] == 0 else 0
        bonus += -7 if self.board[0][7] == 1 else 7 if self.board[0][7] == 0 else 0
        bonus += -7 if self.board[7][0] == 1 else 7 if self.board[7][0] == 0 else 0
        bonus += -7 if self.board[7][7] == 1 else 7 if self.board[7][7] == 0 else 0
        for i in range(1, 7):
            bonus += -2 if self.board[0][i] == 1 else 2 if self.board[0][i] == 0 else 0
            bonus += -2 if self.board[i][0] == 1 else 2 if self.board[i][0] == 0 else 0
            bonus += -2 if self.board[7][i] == 1 else 2 if self.board[7][i] == 0 else 0
            bonus += -2 if self.board[i][7] == 1 else 2 if self.board[i][7] == 0 else 0




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

    def alphabeta_move(self, player, depth, alpha, beta):
        if depth == 0 or self.terminal():
            return self.h(), None

        best_value = float('-inf') if player == 0 else float('inf')
        best_move = None

        moves = self.moves(player)

        for move in moves:
            new_board = Board()
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


# Przeprowadzenie symulacji wielu gier
results = {"Bot 1 wins": 0, "Bot 2 wins": 0, "Draw": 0}
start_time = time.time()
def play_games(results_queue):
    results = {"Bot 1 wins": 0, "Bot 2 wins": 0, "Draw": 0}
    for i in range(10):  # liczba gier do przeprowadzenia
        player = i % 2
        print(f"Game {i + 1} started...")

        B = Board()

        while True:
            if player == 0:
                value, move = B.alphabeta_move(player, depth=5, alpha=float('-inf'), beta=float('inf'))
                B.do_move(move, player)
            else:
                move = B.random_move(player)
                B.do_move(move, player)

            player = 1 - player
            if B.terminal():
                result = "Draw" if B.result() == 0 else "Bot 1 wins" if B.result() > 0 else "Bot 2 wins"
                results[result] += 1
                break
    results_queue.put(results)

def main():
    time_start = time.time()
    num_processes = 20
    results_queue = multiprocessing.Queue()
    processes = []

    for i in range(num_processes):
        process = multiprocessing.Process(target=play_games, args=(results_queue,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    final_results = {"Bot 1 wins": 0, "Bot 2 wins": 0, "Draw": 0}
    while not results_queue.empty():
        results = results_queue.get()
        for key, value in results.items():
            final_results[key] += value

    print("Results:")
    for result, count in final_results.items():
        print(f"{result}: {count}")

    print(f"Time: {time.time() - time_start:.2f}s")

if __name__ == "__main__":
    main()
