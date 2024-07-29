class Balance:
    def __init__(self):
        self.atm_balance = 1000000
        self.account_balance = 30000
        self.transaction_limit = 0

    def display_atm_balance(self):
        print("Available balance in ATM:", self.atm_balance)
        print()

    def authenticate_card(self, card_type):
        self.card_type = card_type.lower()
        if self.card_type == "1" or self.card_type == "rupay":
            self.card_type = "rupay"
            self.transaction_limit = 2000
            return True
        elif self.card_type == "2" or self.card_type == "visa":
            self.card_type = "visa"
            self.transaction_limit = 5000
            return True
        elif self.card_type == "3" or self.card_type == "mastercard":
            self.card_type = "mastercard"
            self.transaction_limit = 8499
            return True
        else:
            print("Invalid selection of card")
            return False

    def check_balance(self):
        print("Available balance in account:", self.account_balance)

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount <= self.account_balance and withdrawal_amount <= self.atm_balance:
            if withdrawal_amount <= self.transaction_limit:
                self.account_balance -= withdrawal_amount
                self.atm_balance -= withdrawal_amount
                self.transaction_limit -= withdrawal_amount
                print(withdrawal_amount, "rupees withdrawn, available balance:", self.account_balance)
                print("Remaining transaction limit:", self.transaction_limit)
            else:
                print("Exceeded transaction limit")
        elif self.account_balance < withdrawal_amount:
            print("Insufficient funds in account")
        elif withdrawal_amount > self.atm_balance:
            print("Insufficient funds in ATM")
        else:
            print("Invalid selection")

    def deposit(self, deposit_amount):
        self.account_balance += deposit_amount
        print(deposit_amount, "rupees deposited, available balance:", self.account_balance)
        print()
