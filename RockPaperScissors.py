import random

intro = input("Type 0 For Rock, 1 for Paper and 2 for Scissors. \n")

if intro == "0":
    print('''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)''')
    

elif intro == "1":
    print('''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)''')

elif intro == "2":
    print('''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)''')
    
computer_choice = random.randint(0, 2)

if computer_choice == 0:
     print("                                                                                         ")
     print("Computer chooses")
     print('''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)''')
    

elif computer_choice == 1:
    print("Computer chooses")
    print('''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)''')

elif computer_choice == 2:
    print("Computer chooses")
    print('''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)''')
    
if intro == "0" and computer_choice == 0:
    print("Its a draw")

elif intro == "0" and computer_choice == 1:
    print("You lost")

elif intro == "0" and computer_choice == 2:
    print("You won!")

elif intro == "1" and computer_choice == 0:
    print("You won!")

elif intro == "1" and computer_choice == 1:
    print("Its a draw")

elif intro == "1" and computer_choice == 2:
    print("You lost")

elif intro == "2" and computer_choice == 0:
    print("You lost")

elif intro == "2" and computer_choice == 1:
    print("You won!")

elif intro == "2" and computer_choice == 2:
    print("Its a draw")

else:
        print("Just dont")
        print("Its annoying")
        print("PLEASE STOP")
        print("IM WARNING YOU")
        print("NOOOOOOOOOOOOOOOOOOOO")
        print("<dies>")