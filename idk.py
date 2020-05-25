import random

class Account():
    def __init__(self, name):
        self.balance = 1500
        self.name = name
        self.account_no = self.generate_acc_no()

    def generate_acc_no(self):
        return random.randint(1000, 9999)

    def account_creation(self):
        name = input("Welcome to <Random Bank Name>, what's your name?")
        userID = print(f"Welcome, your userID is : {random.randint(1,999)}")
        print(f"Your total balance is : {self.initial_amount}")

    
    def deposit(self):
        amount = int(input("How much would you like to deposit: "))
        self.initial_amount += amount
    
    def withdraw(self):
        amount = int(input("How much would you like to withdraw: "))
        self.initial_amount -= amount
    
    def get_balance(self):
        return self.initial_amount
    
    def dump(self):
        s = f"{name}, {userID}, balance: {self.initial_amount}"
        print(s)

if __name__ == '__main__':
    name = input("Welcome to <Random Bank Name>, what's your name?")
    user_account = Account(name)

    
    print('Account holder: ', user_account.name)
    print('Account number: ', user_account.account_no)
    print('Account blance: ', user_account.balance)