import random

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = list(Card(rank, suit) for suit in suits for rank in ranks)
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()