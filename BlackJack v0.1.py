import random

"""HIGH PRIO"""
#TODO: LINE 75
#TODO: LINE 82

"""MEDIUM PRIO"""
#TODO: Make function that gives access whenever game needs to change player's total balance (after winning or losing)
#TODO: LINE 66

"""LOW PRIO"""
#TODO: Use JSON for balance (or mySQL if you hate yourself)

class Deck():
    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4

    def deck_shuffle(self):
        return random.shuffle(self.cards)

    def pop(self, index=-1):
        return self.cards.pop(index)
    
def betting(player_balance):
    while True:
        bet = int(input("How much do you want to bet: "))
        if bet > player_balance:
            print("You cannot bet more than you already have!")
            idfk = input("Would you like to print another amount? (y/n): ")
            if idfk[0].lower() == "y":
                continue
            elif idfk[0].lower() == "n":
                break
        else:
            player_balance -= bet
            return player_balance

def hit(player_hand, dealer_hand):
    while True:
        again = input("Do you want to hit (y/n): ")
        if again[0].lower() == "y":
            player_hand.append(deck.pop())
            if sum(player_hand) > 21:
                print("BUST")
                break
            print(f"Player: {player_hand} [{sum(player_hand)}]")
            continue
        elif again[0].lower() == "n":
            break
        else:
            print("cba now")
            break
    return player_hand, dealer_hand
    


def winner_dealer():
    print("dealer win")
def winner_player():
    print("player win")
        

deck = Deck()
deck.deck_shuffle()
player_hand = []
dealer_hand = []
player_hand.append(deck.pop()) # Find a way to multiply without typing it twice
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_balance = 1500 
player_name = "Nameless One"

#GAME BEGINS
while sum(player_hand) < 21:
    bet = print(f"Welcome, {player_name}, your total balance is: {betting(player_balance)} ") ## BALANCE DOESNT KEEP UP IT RESETS, BUT CARDS DON'T ***HIGH PRIO***
    print(f"Dealer: {dealer_hand},[?] ")
    print(f"Player: {player_hand} [{sum(player_hand)}]")
    hit(player_hand, dealer_hand)
    dealer_hand.append(deck.pop())
    print(f"Dealer: {dealer_hand} [{sum(dealer_hand)}]")
    print(f"Player: {player_hand} [{sum(player_hand)}]")
    if sum(player_hand) > sum(dealer_hand): # Implement proper logic on whos winning when (IF player=21 double etc.) 
        print("play wins lol")
        cont = input("Play again (y/n): ")
        if cont[0].lower() == "y":
            continue
        elif cont[0].lower() == 'n':
            break
        else:
            print("cba now")
            break
    else:
        print("you losts lol")

# # # CORE GAME LOGIC # # #
#  if sum(player_hand) == 21:
#         winner_player()
#     elif sum(dealer_hand) == 21:
#         winner_dealer()
#     elif sum(player_hand) < 22 and sum(player_hand) > sum(dealer_hand):
#         winner_player()