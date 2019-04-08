
class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit (self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print("User ", self.name, " , Balance:  ", self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -=amount
        other_user.account_balance += amount
        return self


bob = User("Bob", "bob@nothing.com")
kim = User("Kim", "kim@nothing.com")
mary = User("Mary", "mary@nothing.com")



#Have the first user make 3 deposits and 1 withdrawal and then display their balance
bob.make_deposit(200).make_deposit(150).make_deposit(50).make_withdrawal(100)
bob.display_user_balance()

#Have the second user make 2 deposits and 2 withdrawals and then display their balance

kim.make_deposit(400).make_deposit(400).make_withdrawal(150).make_withdrawal(150)

kim.display_user_balance()

#3 Have the third user make 1 deposits and 3 withdrawals and then display their balance

mary.make_deposit(800).make_withdrawal(150).make_withdrawal(150).make_withdrawal(150)

mary.display_user_balance()

#BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

bob.transfer_money(mary,75)

print("transfer")

bob.display_user_balance()
mary.display_user_balance()