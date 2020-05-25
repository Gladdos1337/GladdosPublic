#BlackJack v0.1
#TODO: Make a Welcome class, that Greets the user by their name, while also stating their balance.
#TODO: Make a "Deck" class, (Will be added later)


# suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
#          'Queen':10, 'King':10, 'Ace':11}

import random

class Deck():
    def __init__(self):
        self.cards =[2,3,4,5,6,7,8,9,10*3,11] * 4 #This is a deck consisted of Numbers only
                                                  # Improve this waaay later
    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

class Welcome(Deck): # Class that Greets the player & states their balance. ##TODO: Use JSON for balance (or mySQL if you hate yourself)
    def __init__(self, player_name, player_balance):
        super().__init__(cards)
        self.player_name = player_name
        self.player_balance = player_balance
        self.cards = cards
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
                    return self.player_balance
            else:
                self.player_balance -= self.bet
                return self.player_balance
        self.player_balance -= self.bet
    
    def deal():
        pass


    def hit(self):
        pass
        
    
    def __str__(self):
        return(f"Welcome to BlackJack, {self.player_name}, your current balance is {self.player_balance}.")


        
player_balance = 1500
wlc = Welcome("Nameless One", player_balance)
print(wlc.betting())
next_move = input("Would you like to hit or stand")
