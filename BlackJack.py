import random

my_suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
my_ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
my_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
             'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

p1_card1 = ()
p2_card1 = ()
p1_card2 = ()
p2_card2 = ()

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

    def shuffle(self):
        random.shuffle(self.decklist)

    def show(self):
        for card in self.decklist:
            print(card)

    def deal(self):
        card1 = self.decklist.pop()
        return card1




my_deck = Deck()

for s in my_suits:
    for r in my_ranks:
        a = Card(s, r)
        my_deck.addcard(a)

my_deck.shuffle()
#my_deck.show()

p1_card1 = my_deck.deal()
p2_card1 = my_deck.deal()

p1_card2 = my_deck.deal()
p2_card2 = my_deck.deal()
print(f'Player 1 = {p1_card1,p1_card2}')
print(f'Player 1 = {p2_card1,p2_card2}')

f string doesnt work
