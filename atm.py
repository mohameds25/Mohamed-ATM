from account import Account

class ATM:
    def __init__(self, account):
        self.account = account

    def authenticate(self):
        print("\n===== Login Required =====")
        for _ in range(3):  # Allow 3 attempts
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username == self.account.username and password == self.account.password:
                print("Login successful!\n")
                return True
            else:
                print("Incorrect username or password. Try again.")
        print("Too many failed attempts. Exiting...")
        return False

    def display_menu(self):
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def run(self):
        if not self.authenticate():
            return
        
        print(f"Welcome, {self.account.account_holder}!")
        while True:
            self.display_menu()
            choice = input("Select an option (1-4): ")

            if choice == "1":
                balance = self.account.check_balance()
                print(f"Your current balance is: ${balance:.2f}")
            elif choice == "2":
                try:
                    amount = float(input("Enter the amount to deposit: $"))
                    print(self.account.deposit(amount))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == "3":
                try:
                    amount = float(input("Enter the amount to withdraw: $"))
                    print(self.account.withdraw(amount))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")