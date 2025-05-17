print("Welcome to the Vending Machine!!")
print('''Available items:
    A1 - Chocolate Bar - $1.50
    B2 - Chips - $1.00 
    C3 - Soda - $2.00''')

chocolate_bar = 1.50
chips = 1.00
soda = 2.00

def purchase():

    item_choosing = input("Enter the code of the item you want to purchase: \n")

    if item_choosing == "A1" or item_choosing == "a1":
        entered_money = float(input("This item's price is $1.50, please insert your money. \n"))

        if entered_money > chocolate_bar:
            print(f"Please collect your change of ${round((entered_money - chocolate_bar), 2)}")

        elif entered_money < 1.50:
                not_paid_all_chocolate = float(input(f"You haven't paid all of the money to buy this chocolate bar. You have to still pay ${round((chocolate_bar - entered_money), 2)}. Please pay it now. \n"))
                if not_paid_all_chocolate < chocolate_bar:
                    not_paid_all_chocolate
                elif not_paid_all_chocolate == chocolate_bar:
                    print("Thank you for paying!")

    elif item_choosing == "B2" or item_choosing == "b2":
        entered_money = float(input("This item's price is $1.00, please insert your money. \n"))

        if entered_money > chips:
            print(f"Please collect your change of ${round((entered_money - chips), 2)}")

        elif entered_money < 1.00:
                not_paid_all_chips = float(input(f"You haven't paid all of the money to buy these chips. You have to still pay ${round((chips - entered_money), 2)}. Please pay it now. \n"))
                if not_paid_all_chips < chips:
                    not_paid_all_chips
                elif not_paid_all_chips == chips:
                    print("Thank you for paying!")

    elif item_choosing == "C3" or item_choosing == "c3":
        entered_money = float(input("This item's price is $2.00, please insert your money. \n"))

        if entered_money > soda:
            print(f"Please collect your change of ${round((entered_money - soda), 2)}")

        elif entered_money < 2.00:
                not_paid_all_soda = float(input(f"You haven't paid all of the money to buy these chips. You have to still pay ${round((soda - entered_money), 2)}. Please pay it now. \n"))
                if not_paid_all_soda < soda:
                    not_paid_all_soda
                elif not_paid_all_soda == soda:
                    print("Thank you for paying!")

user_choice = '  '


while user_choice != 'x':
     user_choice = input("Press 'r' to purchase , and 'x' to exit the vending machine \n")
     if user_choice == 'r':
          purchase()