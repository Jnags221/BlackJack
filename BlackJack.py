import random

my_suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
my_ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
my_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
             'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

cards = (my_ranks, my_suits)


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank


class Deck:
    def __init__(self):
        self.decklist = []

    def addcard(self, card):
        self.decklist.append(card)


my_deck = Deck()

for s in my_suits:
    for r in my_ranks:
        a = Card(s, r)
        my_deck.addcard(a)