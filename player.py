from deck import Deck
#A player needs to:



#Draw a card
#Play a card
#Collect won cards
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = [] #Hold a stack of cards

    def draw(self):
        
        while len(self.cards) <= 26:
            self.cards.append(Deck.deal())
        return self.cards
    def play(self):
        return self.cards.pop()
    
 

