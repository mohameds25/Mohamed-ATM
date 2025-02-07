class Account:
    def __init__(self, account_holder, balance=0, username="", password=""):
        self.account_holder = account_holder
        self.balance = balance
        self.username = username
        self.password = password

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount:.2f} has been deposited successfully."
        return "Invalid deposit amount. Please try again."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"${amount:.2f} has been withdrawn successfully."
            return "Insufficient funds."
        return "Invalid withdrawal amount. Please try again."