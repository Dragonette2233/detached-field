import dataclasses
import collections
import random


Card = collections.namedtuple('Card', ['rank', 'suit'])
# Jockers = Card('Jocker', 'red'), Card('Jocker', 'black')

@dataclasses.dataclass
class CardsDeck:
    ranks = list('AKQJ') + [str(n) for n in range(10, 1, -1)]
    suits = 'spades diamonds clubs hearts'.split()
    jockers = ('red', 'black')

    def __init__(self):
        self.__cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.__cards += [Card('Jocker', color) for color in self.jockers]

    def __len__(self):
        return len(self.__cards)
    
    def __getitem__(self, key):
        return self.__cards[key]

    def show_deck(self):
        for i in self.__cards: print(i)
        # return self._cards
    
    def get_cards(self, rank: str, suit: str = None) -> list[Card]:
        if suit is None:
            return [card for card in self.__cards if card.rank == rank]
        return [card for card in self.__cards if card.suit == suit and card.rank == rank]

deck = CardsDeck()

k_spades = deck.get_cards(rank='K')

print(k_spades)

def spades_high(card):

    rank_value = list(reversed(CardsDeck.ranks)).index(card.rank)
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    print(rank_value)
    return rank_value * len(suit_values) + suit_values[card.suit]

def sort_this_deck(deck):

    for i in sorted(deck[:-2], key=spades_high):
        print(i)
