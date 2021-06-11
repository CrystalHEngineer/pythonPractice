class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount
        return self

ivan = User("Ivan Asher", "ivan@codingdojo.com")
emory = User("Emory Jesus", "emory@codingdojo.com")
beast = User("Beast", "beast@codingdojo.com")

# ivan = User("Ivan Asher", "ivan@codingdojo.com")
#     .make_deposit(150)
#     .make_deposit(150)
#     .make_deposit(150)
#     .display_user_balance()


ivan.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()

emory.make_deposit(1000).make_deposit(2).make_withdrawal(500).make_withdrawal(200).display_user_balance()

beast.make_deposit(400).make_withdrawal(100).make_withdrawal(50).make_withdrawal(45).display_user_balance()

ivan.transfer_money(emory, 5).display_user_balance()
emory.display_user_balance()