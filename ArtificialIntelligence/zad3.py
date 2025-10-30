# Definicja klasy State:
#
# Ta klasa reprezentuje stan szachownicy.
# Inicjuje się z pozycjami białego króla (w_k_pos), czarnej wieży (rook_pos) i czarnego króla (b_k_pos), oraz z informacją o aktualnym graczu (player).
# Tworzy planszę o wymiarach 8x8 w postaci tablicy dwuwymiarowej.
# Przekształca pozycje pól szachownicy z postaci literowej na numeryczną i odwrotnie.
# Wypełnia planszę ustawiając odpowiednie oznaczenia dla króla i wieży.
# Tworzy listy możliwych ruchów dla białego króla, czarnej wieży i czarnego króla.
# Definicja klasy Node:
#
# Ta klasa reprezentuje węzeł w drzewie przeszukiwań.
# Inicjuje się z danym stanem (state) i opcjonalnie rodzicem (parent).
# Definicja klasy BFS:
#
# Ta klasa implementuje algorytm przeszukiwania wszerz.
# Inicjuje się z początkowym stanem (start_state), pustą kolejką (queue) i zbiorem poprzednich pozycji (previous_pos).
# Dodaje dzieci do aktualnego węzła zgodnie z zasadami gry w szachy.
# Wyprowadza ścieżkę ruchów od aktualnego węzła do korzenia drzewa.
# Wykonuje algorytm przeszukiwania wszerz, dopóki kolejka nie będzie pusta.
# Funkcja execute_debug_case():
#
# Otwiera plik "zad1_input.txt" i dla każdej linii tworzy nowy stan na podstawie danych z pliku.
# Tworzy instancję obiektu BFS dla każdego stanu i wykonuje algorytm przeszukiwania wszerz.
# Rysuje ścieżkę ruchów od znalezionego węzła do korzenia drzewa.
# Funkcja write_path_to_file():
#
# Otwiera plik "zad1_output.txt" do zapisu.
# Dla każdej linii w pliku "zad1_input.txt" tworzy nowy stan na podstawie danych.
# Tworzy instancję obiektu BFS dla każdego stanu i wykonuje algorytm przeszukiwania wszerz.
# Zapisuje ścieżki ruchów od znalezionego węzła do korzenia drzewa do pliku "zad1_output.txt".


class State:
    def __init__(self,player, w_k_pos, rook_pos, b_k_pos):
        self.w_k_pos = w_k_pos
        self.b_k_pos = b_k_pos
        self.rook_pos = rook_pos
        self.player = player

        self.board = [[0 for _ in range(8)] for _ in range(8)]

        self.refactor_pos_to_int()
        self.fill_board()
        self.rook_pos_moves_list = self.rook_pos_moves()
        self.white_king_pos_moves_list = self.white_king_pos_moves()
        self.black_king_pos_moves_list = self.black_king_pos_moves()
        self.refactor_int_to_pos()
        self.all_pos = [self.w_k_pos, self.b_k_pos, self.rook_pos]
        self.refactor_pos_to_int()

    def refactor_pos_to_int(self):
        wk1, wk2 = self.w_k_pos[0], self.w_k_pos[1]
        bk1, bk2 = self.b_k_pos[0], self.b_k_pos[1]
        rk1, rk2 = self.rook_pos[0], self.rook_pos[1]
        self.w_k_pos = self.refactor_one_pos_to_int((wk1, wk2))
        self.b_k_pos = self.refactor_one_pos_to_int((bk1, bk2))
        self.rook_pos = self.refactor_one_pos_to_int((rk1, rk2))

    def refactor_int_to_pos(self):
        wk1, wk2 = self.w_k_pos[0], self.w_k_pos[1]
        bk1, bk2 = self.b_k_pos[0], self.b_k_pos[1]
        rk1, rk2 = self.rook_pos[0], self.rook_pos[1]
        self.w_k_pos = self.refactor_one_int_to_pos((wk1, wk2))
        self.b_k_pos = self.refactor_one_int_to_pos((bk1, bk2))
        self.rook_pos = self.refactor_one_int_to_pos((rk1, rk2))

    def refactor_one_pos_to_int(self, pos):
        refactor_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        return (8 - int(pos[1]), refactor_dict[pos[0]])

    def refactor_one_int_to_pos(self, pos):
        refactor_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return (refactor_dict[pos[1]], 8 - pos[0])

    def fill_board(self):
        self.board[self.w_k_pos[0]][self.w_k_pos[1]] = "WK"
        self.board[self.b_k_pos[0]][self.b_k_pos[1]] = "BK"
        self.board[self.rook_pos[0]][self.rook_pos[1]] = "WR"

    def white_king_pos_moves(self):
        moves = []
        vectors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        b_k_ocupied_fields = [(self.b_k_pos[0] + vector[0], self.b_k_pos[1] + vector[1]) for vector in vectors]
        for vector in vectors:
            new_pos = (self.w_k_pos[0] + vector[0], self.w_k_pos[1] + vector[1])
            if 7 >= new_pos[0] >= 0 and 0 <= new_pos[1] <= 7 and 0 == self.board[new_pos[0]][new_pos[1]] \
                    and new_pos not in b_k_ocupied_fields:
                moves.append(new_pos)
        return moves

    def rook_pos_moves(self):
        moves = []
        vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for vector in vectors:
            new_pos = (self.rook_pos[0] + vector[0], self.rook_pos[1] + vector[1])
            while 7 >= new_pos[0] >= 0 and 0 <= new_pos[1] <= 7 and 0 == self.board[new_pos[0]][new_pos[1]]:
                moves.append(new_pos)
                new_pos = (new_pos[0] + vector[0], new_pos[1] + vector[1])
        return moves

    def is_mat(self):
        if self.black_king_pos_moves_list == [] and self.is_rook_attacking():
            return True
        return False

    def is_rook_attacking(self):
        vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for vector in vectors:
            new_pos = (self.rook_pos[0] + vector[0], self.rook_pos[1] + vector[1])
            while 7 >= new_pos[0] >= 0 and 0 <= new_pos[1] <= 7 and 0 == self.board[new_pos[0]][new_pos[1]]:
                new_pos = (new_pos[0] + vector[0], new_pos[1] + vector[1])
            if new_pos == self.b_k_pos:
                return True
        return False

    def is_pat(self):
        if self.rook_pos == self.b_k_pos:
            return True
        if self.player == 'black' and self.black_king_pos_moves_list == [] and not self.is_rook_attacking():
            return True

    def black_king_pos_moves(self):
        moves = []
        vectors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        vectors2 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        white_king_ocupied_fields = [(self.w_k_pos[0] + vector[0], self.w_k_pos[1] + vector[1]) for vector in vectors]
        white_rook_ocupied_fields = []

        for vector in vectors2:
            new_pos = (self.rook_pos[0] + vector[0], self.rook_pos[1] + vector[1])
            while 7 >= new_pos[0] >= 0 and 0 <= new_pos[1] <= 7 and "WK" != self.board[new_pos[0]][new_pos[1]]:
                white_rook_ocupied_fields.append(new_pos)
                new_pos = (new_pos[0] + vector[0], new_pos[1] + vector[1])


        for vector in vectors:
            new_pos = (self.b_k_pos[0] + vector[0], self.b_k_pos[1] + vector[1])
            if 7 >= new_pos[0] >= 0 and 0 <= new_pos[1] <= 7 and "WK" != self.board[new_pos[0]][new_pos[1]] \
                    and new_pos not in white_king_ocupied_fields and new_pos not in white_rook_ocupied_fields:
                moves.append(new_pos)

        return moves

    def print_board(self):
        print("    A  B  C  D  E  F  G  H")
        for i in range(8):
            print(f"{8 - i} -", end=" ")
            for j in range(8):
                if self.board[i][j] == 0:
                    print("0 ", end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print()
        self.refactor_int_to_pos()
        print(f'White king: {self.w_k_pos}')
        print(f'Black king: {self.b_k_pos}')
        print(f'Rook: {self.rook_pos}')
        self.refactor_pos_to_int()
        print()

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


class BFS:
    def __init__(self, start_state):
        self.current_node = None
        self.start_state = start_state
        self.queue = []
        self.queue.append(Node(start_state))
        self.previous_pos = set()

    def add_children(self):
        if self.current_node.state.is_pat():
            return
        if self.current_node.state.player == 'white':
            for move in self.current_node.state.white_king_pos_moves_list:
                w_k_pos = self.current_node.state.refactor_one_int_to_pos(move)
                b_k_pos = self.current_node.state.refactor_one_int_to_pos(self.current_node.state.b_k_pos)
                rook_pos = self.current_node.state.refactor_one_int_to_pos(self.current_node.state.rook_pos)
                new_pos = (w_k_pos, b_k_pos, rook_pos)
                if new_pos in self.previous_pos:
                    continue
                self.previous_pos.add(new_pos)
                new_state = State('black',w_k_pos,rook_pos, b_k_pos)


                self.queue.append(Node(new_state, self.current_node))

            for move in self.current_node.state.rook_pos_moves_list:
                w_k_pos = self.current_node.state.refactor_one_int_to_pos(self.current_node.state.w_k_pos)
                b_k_pos = self.current_node.state.refactor_one_int_to_pos(self.current_node.state.b_k_pos)
                rook_pos = self.current_node.state.refactor_one_int_to_pos(move)
                new_pos = (w_k_pos, b_k_pos, rook_pos)
                if new_pos in self.previous_pos:
                    continue
                self.previous_pos.add(new_pos)
                new_state = State("black",w_k_pos,rook_pos, b_k_pos)

                self.queue.append(Node(new_state, self.current_node))
        else:
            for move in self.current_node.state.black_king_pos_moves_list:
                w_k_pos = (self.current_node.state.refactor_one_int_to_pos(self.current_node.state.w_k_pos))
                b_k_pos = self.current_node.state.refactor_one_int_to_pos(move)
                rook_pos = self.current_node.state.refactor_one_int_to_pos(self.current_node.state.rook_pos)
                new_pos = (w_k_pos, b_k_pos, rook_pos)
                if new_pos in self.previous_pos:
                    continue

                self.previous_pos.add(new_pos)
                new_state = State('white',w_k_pos, rook_pos,b_k_pos)


                self.queue.append(Node(new_state, self.current_node))

    def draw_path(self, node):
        path = []
        while node:
            path.append(node.state.all_pos)
            node.state.print_board()
            node = node.parent


    def get_path(self, node):
        path = []
        while node:
            path.append(node.state.all_pos)
            node = node.parent
        return path[::-1]

    def play(self):
        while self.queue:
            self.current_node = self.queue.pop(0)
            if self.current_node.state.is_mat():
                return self.current_node
            self.add_children()



def execute_debug_case():
    with open("zad1_input.txt", 'r') as file:
        for linia in file:
            print("next example")
            tab = linia.split()
            new_state = State(tab[0], tab[1], tab[2], tab[3])
            bfs = BFS(new_state)
            node = bfs.play()
            bfs.draw_path(node)

def write_path_to_file():
    file2 = open("zad1_output.txt", 'w')
    with open("zad1_input.txt", 'r') as file:
        for linia in file:
            tab = linia.split()
            new_state = State(tab[0], tab[1], tab[2], tab[3])
            bfs = BFS(new_state)
            node = bfs.play()
            file2.write(str(bfs.get_path(node)) + "\n")

    file2.close()



execute_debug_case()
#write_path_to_file()