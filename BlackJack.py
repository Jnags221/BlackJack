import random

my_suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
my_ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
my_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Cards:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        print(f'{self.value} of {self.rank}')


class Deck:
    def __init__(self, suits, ranks):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                #THIS IS WHERE YOU CREATE CARDS my_cards = Cards(my_suits, my_ranks)
                self.deck.append(Cards(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)
        print(self.deck)



deck = Deck(my_suits, my_ranks)
deck.shuffle()