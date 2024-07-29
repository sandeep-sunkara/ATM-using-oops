import authentication
import tasks

print("//WELCOME TO SA ATM//")
username = input("Enter username: ")
password = input("Enter password: ")

auth_obj = authentication.Auth(username, password)

if auth_obj.authenticate():
    task_obj = tasks.Balance()
    task_obj.display_atm_balance()
    print("Enter card type:")
    print("1. Rupay\n2. Visa\n3. Mastercard")
    card_type = input()
    
    if task_obj.authenticate_card(card_type):
        while True:
            print("Menu:")
            print("1. Check Balance\n2. Withdraw\n3. Deposit\n4. Mini Statement\n5. Exit")
            task = input()

            if task == "1" or task.lower() == "check balance":
                task_obj.check_balance()
                print()
            elif task == "2" or task.lower() == "withdraw":
                withdrawal_amount = int(input("Enter amount to withdraw: "))
                task_obj.withdraw(withdrawal_amount)
            elif task == "3" or task.lower() == "deposit":
                deposit_amount = int(input("Enter amount to deposit: "))
                task_obj.deposit(deposit_amount)
                print()
            elif task == "4" or task.lower() == "mini statement":
                print("CURRENTLY UNAVAILABLE")
                print()
            elif task == "5" or task.lower() == "exit":
                print("THANK YOU FOR USING SA ATM")
                break
            else:
                print("Invalid option")
                print()
