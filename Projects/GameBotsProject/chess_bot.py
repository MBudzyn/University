import chess
import chess.svg
import webbrowser
import random



def parse_move(move):
    return chess.Move.from_uci(move)


class ChessBoard:
    def __init__(self):
        self.board = chess.Board()

    def __str__(self):
        return str(self.board)

    def __copy__(self):
        new_board = ChessBoard()
        new_board.board = self.board.copy()
        return new_board

    def is_white_turn(self):
        return self.board.turn == chess.WHITE

    def count_player_pawns(self, is_white=True):
        if is_white:
            return len(self.board.pieces(chess.PAWN, chess.WHITE))
        else:
            return len(self.board.pieces(chess.PAWN, chess.BLACK))

    def count_player_knights(self, is_white=True):
        if is_white:
            return len(self.board.pieces(chess.KNIGHT, chess.WHITE))
        else:
            return len(self.board.pieces(chess.KNIGHT, chess.BLACK))

    def count_player_bishops(self, is_white=True):
        if is_white:
            return len(self.board.pieces(chess.BISHOP, chess.WHITE))
        else:
            return len(self.board.pieces(chess.BISHOP, chess.BLACK))

    def count_player_rooks(self, is_white=True):
        if is_white:
            return len(self.board.pieces(chess.ROOK, chess.WHITE))
        else:
            return len(self.board.pieces(chess.ROOK, chess.BLACK))

    def count_player_queens(self, is_white=True):
        if is_white:
            return len(self.board.pieces(chess.QUEEN, chess.WHITE))
        else:
            return len(self.board.pieces(chess.QUEEN, chess.BLACK))

    def count_material_value(self, is_white=True):
        return (self.count_player_pawns(is_white) +
                self.count_player_knights(is_white) * 3 +
                self.count_player_bishops(is_white) * 3 +
                self.count_player_rooks(is_white) * 5 +
                self.count_player_queens(is_white) * 9)

    def material_advantage(self, is_white=True):
        if is_white:
            return self.count_material_value() - self.count_material_value(False)
        else:
            return self.count_material_value(False) - self.count_material_value()

    def terminal(self):
        return self.board.is_game_over()

    def is_black_turn(self):
        return self.board.turn == chess.BLACK

    def get_legal_moves(self):
        return self.board.legal_moves

    def make_move(self, m):
        self.board.push(m)

    def undo_last_move(self):
        self.board.pop()

    def visualize(self):
        svg_board = chess.svg.board(self.board, size=700, coordinates=True)
        with open("chess_board.html", "w") as html_file:
            html_file.write('<html><body>\n')
            html_file.write(svg_board)
            html_file.write('\n</body></html>')
        webbrowser.open("chess_board.html")

    def get_random_move(self):
        return random.choice([move for move in self.get_legal_moves()])

    def open_structure_value(self, player):
        pom_board = self.__copy__()
        pom_board.board.turn = not pom_board.board.turn
        ml = list(self.get_legal_moves())
        ml2 = list(pom_board.get_legal_moves())
        if player:
            return len(ml) - len(ml2)
        else:
            return len(ml2) - len(ml)

    


    def count_active_figures_advantage(self,player=True):
        pom_board = self.__copy__()
        pom_board.board.turn = not pom_board.board.turn
        white_p_figures = set()
        black_p_figures = set()

        if self.board.turn:
            for move in self.get_legal_moves():
                white_p_figures.add(str(move)[:2])

            for move in pom_board.get_legal_moves():
                black_p_figures.add(str(move)[:2])

        else:
            for move in self.get_legal_moves():
                black_p_figures.add(str(move)[:2])

            for move in pom_board.get_legal_moves():
                white_p_figures.add(str(move)[:2])

        if player:
            return (len(white_p_figures) - self.count_player_pawns(True)
                    - len(black_p_figures) + self.count_player_pawns(False))
        else:
            return (len(black_p_figures) - self.count_player_pawns(False)
                    - len(white_p_figures) + self.count_player_pawns(True))




    def alphabeta(self, depth, alpha, beta, is_maxing=True, player=True):
        if depth == 0 or self.terminal():
            return (self.material_advantage(player)
                    + self.open_structure_value(player) * 0.1
                    + self.count_active_figures_advantage(player) * 0.4, None)

        best_value = float('-inf') if is_maxing else float('inf')  # Corrected this line
        best_move = None

        moves = self.get_legal_moves()

        for move in moves:
            new_board = self.__copy__()
            new_board.make_move(move)

            value, _ = new_board.alphabeta(depth - 1, alpha, beta, not is_maxing, player)

            if is_maxing:
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

    def play_game_wrandom(self):
        while not self.board.is_game_over():
            self.visualize()
            if self.is_white_turn():
                move = input("Enter move: ")
                move = parse_move(move)
                if move in self.get_legal_moves():
                    self.make_move(move)
                else:
                    print("Invalid move")
            else:
                print("Thinking...")
                move = self.get_random_move()
                self.make_move(move)
        self.visualize()
        print("Game over")

    def play_game_walphabeta(self, depth=4):
        while not self.board.is_game_over():
            self.visualize()
            if self.is_white_turn():
                move = input("Enter move: ")
                move = parse_move(move)
                if move in self.get_legal_moves():
                    self.make_move(move)
                    print(self.open_structure_value(True), self.board.turn)
                    print(self.count_active_figures_advantage(True), "g", True)
                else:
                    print("Invalid move")
            else:
                print("Thinking...")
                _, move = self.alphabeta(depth, float('-inf'), float('inf'), True, False)
                self.make_move(move)
                print(self.open_structure_value(False), self.board.turn)
                print(self.count_active_figures_advantage(False), "k", False)



def main():
    board = ChessBoard()

    board2 = chess.Board()
    print(board2.pieces(chess.PAWN, chess.WHITE))
    print(board.count_material_value())


    board.play_game_walphabeta(3)


if __name__ == "__main__":
    main()
