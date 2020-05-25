import random

class Account():
    def __init__(self, name):
        self.balance = 1500
        self.name = name
        self.account_no = self.generate_acc_no()

    def generate_acc_no(self):
        return random.randint(1000, 9999)

    def deposit(self):
        amount = int(input("How much would you like to deposit: "))
        self.balance += amount
    
    def withdraw(self):
        amount = int(input("How much would you like to withdraw: "))
        self.balance -= amount
    
    def get_balance(self):
        return self.balance

name = input("Welcome to <Random Bank Name>, what's your name?")
user_account = Account(name)

print('Account holder: ', user_account.name)
print('Account number: ', user_account.account_no)
print('Account blance: ', user_account.get_balance())