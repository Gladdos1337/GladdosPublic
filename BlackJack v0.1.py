import random, sys

"""HIGH PRIO"""
#TODO: Make function that gives access whenever game needs to change player's total balance (after winning or losing)

"""MEDIUM PRIO"""
#TODO: Refactor the code

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
            if sum(player_hand) == 21:
                print("Player Blackjack in hit function")
                break
            if sum(player_hand) > 21:
                break
            print(f"Player: {player_hand} [{sum(player_hand)}]")
            continue
        elif again[0].lower() == "n":
            break
        else:
            print("cba now")
            break
    return player_hand, dealer_hand

def append_dealer_hand(dealer_hand,player_hand):
    while sum(player_hand) != 21:
        if sum(dealer_hand) < 17:
            dealer_hand.append(deck.pop())
            if sum(dealer_hand) > sum(player_hand):
                print("dealer wins")
                return dealer_hand,player_hand
            if sum(dealer_hand) > 21:
                print("Dealer Bust, player wins!")
                return dealer_hand,player_hand
        else:
            break

def blackJack(player_hand, dealer_hand):
    if sum(player_hand) == 21 and sum(dealer_hand) != 21:
        print("Blackjack!")
        print("ADD 2x betting win later on.")
        game_active = False

# def lose(player_hand, dealer_hand):  ## UNUSED FOR NOW
#     if sum(player_hand) > 21: 
#         print("player loses from a fucntion")
#         game_active = False
#     if sum(dealer_hand) > 21:
#         print("dealeer loses from a fucntion")
#         game_active = False


deck = Deck()
deck.deck_shuffle()
player_hand = []
dealer_hand = []
player_hand.append(deck.pop()) # Find a way to multiply without typing it twice
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_balance = 1500 
player_name = "Nameless One"
game_active = True


#GAME BEGINS

while True:
    while game_active == True:
        bet = print(f"Welcome, {player_name}, your total balance is: {betting(player_balance)} ") ## BALANCE DOESNT KEEP UP IT RESETS, BUT CARDS DON'T ***HIGH PRIO***
        print(f"Dealer: {dealer_hand},[?] ")
        print(f"Player: {player_hand} [{sum(player_hand)}]")
        blackJack(player_hand, dealer_hand)
        while True:
            hit_or_stand = input("Do you want to hit or stand (h/s): ")
            if hit_or_stand[0] == 'h': # HIT
                hit(player_hand, dealer_hand)
                dealer_hand.append(deck.pop())
                if sum(player_hand) > 21:
                    break
                append_dealer_hand(dealer_hand,player_hand)
                if sum(player_hand) > 21:
                    game_active = False
                    break
                else:
                        # i have no fucking idea why it got stucked here
                        print("stuck @ 97")
                        break
            elif hit_or_stand[0] == 's': # STAND
                append_dealer_hand(dealer_hand,player_hand)
                break
        print(f"Dealer: {dealer_hand} [{sum(dealer_hand)}]")
        print(f"Player: {player_hand} [{sum(player_hand)}]")
        if sum(player_hand) == 21 and sum(dealer_hand) != 21: # If player gets blackjack
            print("Player wins!")
            break
        if sum(player_hand) == 21 and sum(dealer_hand) == 21:
            print("It do be even tho")
            break
        #WINNING LOGIC
        if sum(player_hand) > 21:
            print("Player bust, House wins. 131")
            break
        if sum(dealer_hand) > 21:
            print("Dealer bust, player wins.")
            break
        if sum(player_hand) < sum(dealer_hand): # Implement proper logic on whos winning when (IF player=21 double etc.) 
            break
        elif sum(player_hand) > sum(dealer_hand):
            if sum(dealer_hand) < 17 and sum(dealer_hand) > sum(player_hand):
                while sum(dealer_hand) > 21:
                    dealer_hand.append(deck.pop())
                    if sum(dealer_hand) > sum(player_hand):
                        print("House wins.")
                        game_active = False
                        break
    #In the first while loop:
                    
    again = input("Play again (y/n): ")
    if again[0].lower() == 'y':
        player_hand = []
        dealer_hand = []
        player_hand.append(deck.pop()) # Find a way to multiply without typing it twice
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        game_active = True
    elif again[0].lower() == 'n':
        break
    else:
        print("idk")
        break