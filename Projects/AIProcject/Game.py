
from Auction import Auction
from Player import Player
from typeguard import *
from GlobalVariables import MELD_POINTS_DICT
import logging
import pygame
from CardsManipulator import CardsManipulator
from Card import Card

logging.basicConfig(level=logging.DEBUG)

def winning_card(cards_in_order: list['Card'], trump) -> 'Card':
    if cards_in_order[1].can_beat(cards_in_order[0], trump):
        if cards_in_order[2].can_beat(cards_in_order[1], trump):
            return cards_in_order[2]
        else:
            return cards_in_order[1]
    else:
        if cards_in_order[2].can_beat(cards_in_order[0], trump):
            return cards_in_order[2]
        else:
            return cards_in_order[0]

@typechecked
class Game:
    def __init__(self, auction: 'Auction'):
        self.players_in_order: list['Player'] = auction.players_in_order
        self.cards_manipulator = CardsManipulator()
        self.playing_player_index: int = auction.active_player_index
        self.trick_pile: list['Card'] = []
        self.trump = None
        #self.init_pygame()

    def get_player_by_index(self, index: int) -> 'Player':
        return self.players_in_order[index]

    def split_two_cards(self):
        two_cards = self.get_player_by_index(self.playing_player_index).discard_two_cards()
        self.get_player_by_index((self.playing_player_index - 1) % 3).add_card_to_hand(two_cards[0])
        self.get_player_by_index((self.playing_player_index + 1) % 3).add_card_to_hand(two_cards[1])

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1600, 1000))
        pygame.display.set_caption('Thousand Card Game')
        self.card_images = self.load_card_images()
        self.background = pygame.image.load('graphics/board.png')
        self.font = pygame.font.Font(None, 36)
        self.player_positions = [(750, 800), (1400, 300), (100, 300)]  # Pozycje kart graczy

    def load_card_images(self):
        card_images = {}
        for suit in ["H", "D", "C", "S"]:
            for rank in ["N", "T", "J", "Q", "K", "A"]:
                card_images[f'{rank}{suit}'] = pygame.image.load(f'graphics/{rank}{suit}.png')
        return card_images

    def actualize_after_round(self, cards_in_order: list['Card']):
        w_card = winning_card(cards_in_order, self.trump)
        card_ind = cards_in_order.index(w_card)
        winner_index = (self.playing_player_index + card_ind) % 3
        self.players_in_order[winner_index].trick_pile += cards_in_order
        self.players_in_order[winner_index].sum_of_points_in_actual_round += sum([card.value for card in cards_in_order])
        self.playing_player_index = winner_index

    def get_all_players_tricks(self):
        return (self.get_player_by_index(0).trick_pile +
                self.get_player_by_index(1).trick_pile +
                self.get_player_by_index(2).trick_pile)

    def play_one_round(self) -> list['Card']:
        cards_in_order = [None, None, None]
        current_player_index = self.playing_player_index
        cards_in_order[0] = self.get_player_by_index(self.playing_player_index).play_card(None, None, self.trump, self.get_all_players_tricks())

        if self.get_player_by_index(self.playing_player_index).is_melding(cards_in_order[0]):
            print(f"Player {current_player_index + 1} melds!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! {cards_in_order[0]}")
            self.get_player_by_index(self.playing_player_index).sum_of_points_in_actual_round += MELD_POINTS_DICT[cards_in_order[0].suit]
            self.trump = cards_in_order[0].suit
        print(f"Player {current_player_index + 1} played {cards_in_order[0]}")

        for j in range(1, 3):
            current_player_index = (self.playing_player_index + j) % 3
            cards_in_order[j] = self.players_in_order[current_player_index].play_card(cards_in_order[0],
                                                                                      cards_in_order[1],
                                                                                      self.trump, self.get_all_players_tricks())
            print(f"Player {current_player_index + 1} played {cards_in_order[j]}")

        return cards_in_order

    def print_cards(self, cards_in_order):
        self.screen.blit(self.background, (0, 0))

        # Rysuj karty graczy
        self.draw_player_hands()

        # Rysuj trick piles
        self.draw_trick_piles()

        # Rysuj karty na stole
        positions = [(650, 500), (800, 300), (500, 300)]  # Pozycje kart na stole
        for i, card in enumerate(cards_in_order):
            if card:
                card_image = self.card_images[f'{card.rank}{card.suit}']
                self.screen.blit(card_image, positions[i])
                pygame.display.flip()
                self.wait_for_click()

    def draw_player_hands(self):
        for i, player in enumerate(self.players_in_order):
            player_hand = player.hand
            for j, card in enumerate(player_hand):
                card_image = self.card_images[f'{card.rank}{card.suit}']
                self.screen.blit(card_image, (self.player_positions[i][0] + 60 * j, self.player_positions[i][1]))

    def draw_trick_piles(self):
        trick_positions = [(100, 400), (1200, 300), (750, 800)]  # Pozycje stosów zebranych kart
        for i, player in enumerate(self.players_in_order):
            trick_pile = player.trick_pile
            for j, card in enumerate(trick_pile):
                card_image = self.card_images[f'{card.rank}{card.suit}']
                self.screen.blit(card_image, (trick_positions[i][0] + 20 * (j % 10), trick_positions[i][1] + 30 * (j // 10)))

    def wait_for_click(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    def actualize_after_game(self):
        for player in self.players_in_order:
            player.trick_pile = []
            if player.is_declarer:
                if player.sum_of_points_in_actual_round >= player.points_to_play:
                    player.sum_of_points += player.points_to_play
                else:
                    player.sum_of_points -= player.points_to_play
            else:
                player.sum_of_points += ((player.sum_of_points_in_actual_round + 5) // 10) * 10

            player.sum_of_points_in_actual_round = 0
            player.actual_value_in_auction = 0

    def print_data(self):
        for k in range(3):
            player_index = (self.playing_player_index + k) % 3
            print(
                f"Player {player_index + 1} remaining hand: {[str(card) for card in self.players_in_order[player_index].hand]}")

        # Print the trick pile and sum of points for each player
        for k in range(3):
            print(f"Player {k + 1} trick pile: {[str(card) for card in self.players_in_order[k].trick_pile]}")
            print(f"Player {k + 1} sum of points: {self.players_in_order[k].sum_of_points}")

        if self.trump:
            print(f"Current trump: {self.trump}")
        else:
            print("No trump declared yet")

    def play(self, _print: bool = False):
        self.split_two_cards()
        self.get_player_by_index(self.playing_player_index).begin_of_playing_round()
        for i in range(8):
            cards_in_order = self.play_one_round()
            self.actualize_after_round(cards_in_order)
            if _print:
                self.print_cards(cards_in_order)
            self.print_data()
        self.actualize_after_game()






