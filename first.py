import random

# class Deck():
#     def __init__(self):
#         self.cards =[2,3,4,5,6,7,8,9,10*3,11] * 4 #This is a deck consisted of Numbers only
#                                                   # Improve this waaay later
#     def shuffle(self):
#         random.shuffle(self.cards)
#         return self.cards

def deck(cards):
    random.shuffle(cards)
    return cards

class Welcome(): # Class that Greets the player & states their balance. ##TODO: Use JSON for balance (or mySQL if you hate yourself)
    def __init__(self, player_name, player_balance):
        self.player_name = player_name
        self.player_balance = player_balance
        self.player_hand = deck(cards).pop(1), deck(cards).pop(1)
        self.dealer_hand = deck(cards).pop(1), deck(cards).pop(1)
    def betting(self):
        while True:
            self.bet = int(input("How much do you want to bet: "))
            if self.bet > self.player_balance: 
                print("You cannot bet more than you already have!")
                idfk = input("Would you like to print another amount? (y/n): ")
                if idfk[0].lower() == "y":
                    continue
                elif idfk[0].lower() == "n":
                    break
                else:
                    print("You answered incorrectly, exiting...")
                    return f"You sucessfully bet: {self.bet}, your balance is: {self.player_balance}"
            else:
                self.player_balance -= self.bet
                return f"You sucessfully bet: {self.bet}, your balance is: {self.player_balance}"
        return f"Your balance is: {self.player_balance}"

    def deal_player(self):
        return f"Player Cards: {self.player_hand}"

    def deal_dealer(self):
        return f"Dealer Cards: {self.dealer_hand}"

    def hit(self):
        self.player_hand += deck(cards).pop(1)
        return self.player_hand

    #Add double in future

    def __str__(self):
        return(f"Welcome to BlackJack, {self.player_name}, your current balance is {self.player_balance}.")

cards =[2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
player_balance = 1500
wlc = Welcome("Nameless One", player_balance)
print(wlc)
print(wlc.deal_player())
print(wlc.deal_dealer())
player_active = True
if player_active == False:
    break
print(wlc.betting())
while player_active == True: #Game begins
    next_move = input("Would you like to hit or stand: ")
    if next_move[0].lower() == "h":
        if sum(wlc.deal_player()) != 21 and sum(wlc.deal_player()) > 21:
            print(wlc.hit())
            break
        else:
            print("You lost") #Improve with function for losing
            break
    elif next_move[0].lower() == "s":

        '''``` SEMI PSUEDO CODE STARTS HERE ```'''
        while player_hand is not 21 and player_hand is not > 21:
            while dealer_hand < 17:
                dealer_hand += deck(cards).pop(1)
                if dealer_hand >= 17 and dealer_hand > player_hand:
                    print("Dealer wins!!!")
                elif dealer_hand >= 17 and dealer_hand < player_hand:
                    print("Player wins")
                    player_balance += bet * 2
        
 


