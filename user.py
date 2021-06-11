class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate= 0.02, balance= 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account.balance}")
    def transfer_money(self, other_user, amount):
        other_user.account.deposit(amount)
        self.account.withdraw(amount)
    def example_method(self):
        self.account.deposit(100)
        print(self.account.balance)

class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient Funds: Charging $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance * self.int_rate
            return self

ivan = User("Ivan Asher", "ivan@codingdojo.com")
emory = User("Emory Jesus", "emory@codingdojo.com")
beast = User("Beast", "beast@codingdojo.com")

ivan.make_deposit(40)
ivan.make_deposit(50)
ivan.make_deposit(600)
ivan.make_withdrawal(500)
ivan.display_user_balance()

emory.make_deposit(1000)
emory.make_deposit(2)
emory.make_withdrawal(500)
emory.make_withdrawal(200)
emory.display_user_balance()

beast.make_deposit(400)
beast.make_withdrawal(100)
beast.make_withdrawal(50)
beast.make_withdrawal(45)
beast.display_user_balance()

ivan.transfer_money(emory, 5)
ivan.display_user_balance()
emory.display_user_balance()

