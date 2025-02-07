from account import Account
from atm import ATM

if __name__ == "__main__":
    user_account = Account(account_holder="Mohamed", balance=500, username="moha", password="1234")
    atm = ATM(account=user_account)

    atm.run()