
class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance   
        print("test me again")     
        #balance will either be what the user puts in, or will be 100

    def deposit (self, amount):
        self.balance += amount
        return self

    def withdrawal (self, amount):
        self.balance -= amount
        if self.balance<amount:
            self.balance -=5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -=amount
        return self
        

    def display_account_info(self):
        print("Balance:  ", self.balance)
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance=self.balance*(1+self.int_rate)
        return self

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        print("hehe")
        self.account = BankAccount(int_rate=0.02, balance=0)  #added this line

    def make_deposit (self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self,amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self):
        print("User ", self.name, " , Balance:  ", self.account.balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdrawal(amount)
        other_user.account.deposit(amount)
        return self

    def example_method (self):
        self.account.deposit(100)
        print("asdf", self.account.balance)


bob = User("Bob", "bob@nothing.com")
kim = User("Kim", "kim@nothing.com")
mary = User("Mary", "mary@nothing.com")

bob.make_deposit(10000000000)
bob.display_user_balance()


# Have the first user make 3 deposits and 1 withdrawal and then display their balance
bob.make_deposit(200)
bob.make_deposit(150)
bob.make_deposit(50)
bob.make_withdrawal(100)
bob.display_user_balance()


number1 = BankAccount(.03,1000)
number2 = BankAccount(.02,2000)

number1.deposit(100).deposit(150).deposit(200).withdrawal(75).yield_interest().display_account_info()

number2.deposit(100).deposit(150).withdrawal(75).withdrawal(785).withdrawal(75).withdrawal(75).yield_interest().display_account_info()

#number1.display_account_info()