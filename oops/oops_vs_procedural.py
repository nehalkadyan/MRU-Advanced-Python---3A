# procedural programming

# Small Bank App Functionality
# Several functionalities - deposit to bank,
#  withdraw from bank, check current balance

account_number = "AC1003"
name = "John Doe"
balance = 100000

def deposit(amount):
    # create global balance
    global balance

    # check if amount is more than 0 to deposit it
    if amount > 0:
        balance += amount
        print(f"Deposited amount : {amount}")
    else:
        print("Invalid amount")

def withdraw_from_bank(amount):
    # create global balance
    global balance

    # check if amount is greater than the balance,
    #  if yes don't allow
    if amount <= balance:
        balance -= amount
        print(f"Amount withdrawn : {amount}")

# check balance

def check_balance():
    print(f"Current Balance is : {balance}")

# deposit(5000)
# withdraw_from_bank(15000)
# # check current balance
# check_balance()

# Converting Procedural Approach into Object Oriented 

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount : {amount}")
        else:
            print("Invalid amount")

    def withdraw_from_bank(self,amount):
    # check if amount is greater than the balance,
    #  if yes don't allow
        if amount <= self.balance:
            self.balance -= amount
            print(f"Amount withdrawn : {amount}")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print(f"Current Balance is : {self.balance}")
# object from class -> Bank Account
user1 = BankAccount("AC1003", "John Doe", 100000)
user1.check_balance()





    