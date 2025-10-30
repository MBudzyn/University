# Posiadamy klase gracza przeechowującą wszystkie prawdopodobieństwa uzyskania konkretnego
# układu w zależności od ilości kolorów i 4 tzn pełna talia 4 kolory 13 czwórek
# wszystkie prawdopodobieństwa umieszczamy w tablicy i liczymy prawdopodbieństwo warunkowe
# wygranej gracza wiedząc ,że będzie wygrywał wszytkie remisy ( ma wyższe karty )

import math


class Player:
    def __init__(self, number_of_fours,number_of_colors, wins_draws):
        self.number_of_fours = number_of_fours
        self.number_of_colors = number_of_colors
        self.wins_draws = wins_draws
        self.one_pair_probability = 0
        self.two_pairs_probability = 0
        self.three_of_a_kind_probability = 0
        self.straight_probability = 0
        self.full_house_probability = 0
        self.four_of_a_kind_probability = 0
        self.flush_probability = 0
        self.straight_flush_probability = 0
        self.higher_card_probability = 0
        self.all_combinations = math.comb(self.number_of_fours * self.number_of_colors, 5)
        self.calculate_probabilities()
        self.all_probabilities = [self. higher_card_probability,self.one_pair_probability, self.two_pairs_probability,
                                  self.three_of_a_kind_probability, self.straight_probability, self.flush_probability,
                                  self.full_house_probability,self.four_of_a_kind_probability, self.straight_flush_probability]

        self.sum_of_probabilities = self.one_pair_probability + self.two_pairs_probability + self.three_of_a_kind_probability \
                                      + self.straight_probability + self.full_house_probability + self.four_of_a_kind_probability \
                                      + self.flush_probability + self.straight_flush_probability + self.higher_card_probability

    def calculate_probabilities(self):
        if self.number_of_colors * self.number_of_fours < 5:
            return
        if self.number_of_colors < 2 or self.number_of_fours < 4:
            self.one_pair_probability = 0
        else:
            self.one_pair_probability = self.number_of_fours * math.comb(self.number_of_colors, 2) \
                                        * (self.number_of_fours - 1) * self.number_of_colors \
                                        * (self.number_of_fours - 2) * self.number_of_colors \
                                        * (self.number_of_fours - 3) * self.number_of_colors / 6 / self.all_combinations

        if self.number_of_colors < 2 or self.number_of_fours < 3:
            self.two_pairs_probability = 0
        else:
            self.two_pairs_probability = (math.comb(self.number_of_fours, 2) * math.comb(self.number_of_colors,2)
                                         * math.comb(self.number_of_colors, 2)
                                         * (self.number_of_fours - 2) * self.number_of_colors / self.all_combinations)

        if self.number_of_colors < 3 or self.number_of_fours < 2:
            self.full_house_probability = 0

        else:
            self.full_house_probability = self.number_of_fours * math.comb(self.number_of_colors , 3) \
                                      * (self.number_of_fours - 1) * math.comb(self.number_of_colors , 2) / self.all_combinations
        if self.number_of_colors < 3 or self.number_of_fours < 3:
            self.three_of_a_kind_probability = 0

        else:

             self.three_of_a_kind_probability = (self.number_of_fours * math.comb(self.number_of_colors, 3) *
                                                (self.number_of_fours - 1) * (self.number_of_fours-2) * self.number_of_colors *
                                                self.number_of_colors/2/ self.all_combinations)




        if self.number_of_colors < 4 or self.number_of_fours < 2:
            self.four_of_a_kind_probability = 0
        else:
            self.four_of_a_kind_probability = (self.number_of_fours * (self.number_of_fours - 1)
                                               * self.number_of_colors / self.all_combinations)

        if self.number_of_fours < 5:
            self.straight_flush_probability = 0
            self.flush_probability = 0
            self.straight_probability = 0
        else:
            self.straight_flush_probability = (self.number_of_colors
                                            * (self.number_of_fours - 4) / self.all_combinations)
            self.flush_probability = (self.number_of_colors * math.comb(self.number_of_fours, 5)
                                    / self.all_combinations - self.straight_flush_probability)
            self.straight_probability = (self.number_of_colors ** 5 *
                                        (self.number_of_fours - 4) / self.all_combinations - self.straight_flush_probability)

        self.higher_card_probability = 1 - self.one_pair_probability - self.two_pairs_probability - self.three_of_a_kind_probability \
                                           - self.straight_probability - self.full_house_probability - self.four_of_a_kind_probability \
                                           - self.flush_probability - self.straight_flush_probability






    def print_probabilities(self):
        print(f'One pair probability: {self.one_pair_probability * 100}')
        print(f'Two pairs probability: {self.two_pairs_probability * 100}')
        print(f'Three of a kind probability: {self.three_of_a_kind_probability * 100}')
        print(f'Straight probability: {self.straight_probability * 100}')
        print(f'Full house probability: {self.full_house_probability * 100}')
        print(f'Four of a kind probability: {self.four_of_a_kind_probability * 100}')
        print(f'Flush probability: {self.flush_probability * 100}')
        print(f'Straight flush probability: {self.straight_flush_probability * 100}')
        print(f'Higher card probability: {self.higher_card_probability * 100}')
        print(f'Sum of probabilities: {self.sum_of_probabilities * 100}')



def calculate_win_P2(player1, p2_num_of_colors, p2_num_of_fours):
    win_probability = 0
    player2 = Player(p2_num_of_fours, p2_num_of_colors, 0)
    for i in range(len(player1.all_probabilities)):
        for j in range(i):
            win_probability += player1.all_probabilities[j] * player2.all_probabilities[i]
    return 100 - win_probability * 100



player = Player(4, 4,0)
player3 = Player(13, 4,0)
player3.print_probabilities()
player.print_probabilities()

for i in range(2, 10):
    for j in range(1, 5):
       print(f'Number of colors: {j}, Number of fours: {i}', end=' ')
       print(f'Win probability: {calculate_win_P2(player, j, i)}')