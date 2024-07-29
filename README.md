#ATM System
This project implements an ATM system using Object-Oriented Programming (OOP) concepts in Python. The system supports basic ATM functionalities such as user authentication, balance inquiry, cash withdrawal, cash deposit, and card type handling.

Features
User Authentication: Secure login system to authenticate users.
Card Types: Supports Rupay, Visa, and Mastercard with specific transaction limits.
Balance Inquiry: Check available balance in the user's account.
Cash Withdrawal: Withdraw cash from the user's account within transaction limits.
Cash Deposit: Deposit cash into the user's account.
ATM Balance Display: Show the remaining amount in the ATM.
Technologies Used
Python
Object-Oriented Programming (OOP)
Class Structure
Auth Class
Handles user authentication.

Methods:
__init__(self, username, password): Initializes the class with username and password.
authenticate(self): Authenticates the user based on provided credentials.
Balance Class
Handles ATM and account transactions.

Methods:
__init__(self): Initializes ATM and account balances.
display_atm_balance(self): Displays the remaining amount in the ATM.
authenticate_card(self, card_type): Authenticates the card type and sets the transaction limit.
check_balance(self): Displays the available balance in the user's account.
withdraw(self, withdrawal_amount): Withdraws the specified amount if within limits and updates balances.
deposit(self, deposit_amount): Deposits the specified amount and updates the account balance.


Prerequisites:
Python 3.x installed on your machine.
