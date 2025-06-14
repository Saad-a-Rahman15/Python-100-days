print("This ATM has been placed here by the Mars government. Don't mess around.")
print("If you want to access it, the PIN is 1546.")
print("           ")
print("           ")  
account = 500
pincode = input("Please enter the PIN \n")

if pincode == "1546":
    print("Correct")
    atm_choice = input("You have 3 choices: Press 1 for Withdraw, 2 for Deposit, and 3 for Display. Choose one of these options to continue. \n")
    if atm_choice == "1":
        withdraw = int(input("Enter the amount of money you wish to withdraw: \n"))
        if withdraw > account:
            print("You cannot withdraw because of the fact that you do not have enough money to withdraw this amount")
        elif withdraw < account:
            print(f"You have withdrawn ${withdraw}")
            print(f"Your balance is now ${account - withdraw}")

    elif atm_choice == '2':
        deposit = int(input("Enter the amount of money you wish to deposit: \n"))
        print(f"You have deposited ${deposit}")
        print(f"Your balance is now ${account + deposit}")

    elif atm_choice == '3':
        print(account)
else:
    print("Wrong code.")
    exit
