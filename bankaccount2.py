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


account1 = BankAccount(.01, 100).deposit(5).deposit(5).deposit(5).withdraw(5).yield_interest().display_account_info()

account2 = BankAccount(.01, 200).deposit(10).deposit(10).withdraw(1).withdraw(1).withdraw(1).withdraw(1).yield_interest().display_account_info()

