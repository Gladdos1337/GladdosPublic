import random
 
#TODO: Move Welcome() class to main game loop, only make classes for Deck & Player hands
#TODO: Use JSON for balance (or mySQL if you hate yourself)

class Deck():
    def __init__(self,cards):
        self.cards = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
 
    def deck_shuffle(self):
        return random.shuffle(self.cards)

# deck(cards).pop(1)*2

class Hand():
    #Give it an unique shuffled hand (both for dealer and player)
    pass

def betting():
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
                print("You answered incorrectly, exiting...")
                return f"You sucessfully bet: {bet}, your balance is: {player_balance}"
        else:
            player_balance -= bet
            return f"You sucessfully bet: {bet}, your balance is: {player_balance}"
        return f"Your balance is: {player_balance}"

def winner():
    while player_hand != 21 and player_hand > 21:
        while dealer_hand < 17:
            dealer_hand += deck(cards).pop(1)
            if dealer_hand >= 17 and dealer_hand > player_hand:
                print("Dealer wins!!!")
            elif dealer_hand >= 17 and dealer_hand < player_hand:
                print("Player wins")
                player_balance += bet * 2


player_balance = 1500 #put in simple func that is access whenever game needs to change player's total balance (after winning or losing)
player_name = "Nameless One"
player_active = True
betting()
while player_active == True: #Game begins
    print("Welcome to BlackJack, {player_name}, your current balance is {player_balance}.")
    next_move = input("Would you like to hit or stand: ")
    if next_move[0].lower() == "h":
        if sum(wlc.deal_player()) != 21 and sum(wlc.deal_player()) > 21:
            print(wlc.hit())
            break
        else:
            print("You lost") #Improve with function for losing
            break
    elif next_move[0].lower() == "s":
        # Logic for winner
        winner()
    if player_active == False:
        break