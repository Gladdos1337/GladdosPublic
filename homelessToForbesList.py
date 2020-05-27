import random
class Deck():
    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4

    def deck_shuffle(self):
        return random.shuffle(self.cards)

    def pop(self, index=-1):
        return self.cards.pop(index)


deck = Deck()
deck.deck_shuffle()
player_hand = []
player_hand.append(deck.pop())
player_hand.append(deck.pop())
print((player_hand))