from typeguard import *
from GlobalVariables import RANK_VALUE_DICT, QUALITY_DICT


@typechecked
class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = RANK_VALUE_DICT[rank]
        self.quality = QUALITY_DICT[rank]

    def __gt__(self, other: 'Card') -> bool:
        return self.value > other.value

    def __lt__(self, other: 'Card') -> bool:
        return self.value < other.value

    def __copy__(self):
        return Card(self.rank, self.suit)

    def __str__(self) -> str:
        return f"{self.rank}-{self.suit}"

    def __eq__(self, other: 'Card') -> bool:
        return self.rank == other.rank and self.suit == other.suit

    def can_beat(self, other: 'Card', trump) -> bool:
        if self.suit == other.suit:
            return self > other
        elif self.suit == trump:
            return True
        else:
            return False

    def is_part_of_meld(self) -> bool:
        return self.rank in ['Q', 'K']

    def is_meld(self, other: 'Card') -> bool:
        return self.is_part_of_meld() and other.is_part_of_meld() and \
            self.rank != other.rank and self.suit == other.suit


