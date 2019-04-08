
class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.account_balance = balance
        #balance will either be what the user puts in, or will be 100

    def deposit (self, amount):
        self.account_balance += amount
        return self

    def withdrawal (self, amount):
        self.account_balance -= amount
        if self.account_balance<amount:
            self.account_balance -=5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.account_balance -=amount
        return self
        

    def display_account_info(self):
        print("Balance:  ", self.account_balance)
        return self

    def yield_interest(self):
        if self.account_balance>0:
            self.account_balance=self.account_balance*(1+self.int_rate)
        return self

number1 = BankAccount(.03,1000)
number2 = BankAccount(.02,2000)

number1.deposit(100).deposit(150).deposit(200).withdrawal(75).yield_interest().display_account_info()

number2.deposit(100).deposit(150).withdrawal(75).withdrawal(785).withdrawal(75).withdrawal(75).yield_interest().display_account_info()

#number1.display_account_info()