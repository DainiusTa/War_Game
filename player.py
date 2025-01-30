from deck import Card, Deck
#A player needs to:

#Hold a stack of cards
#Play a card
#Collect won cards
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []