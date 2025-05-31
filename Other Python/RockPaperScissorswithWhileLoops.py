import random

print("Welcome to the Rock Paper Scissors duel!")

user_input = int(input('''1 = Rock
2 = Paper
3 =  Scissors \n'''))

def rock_paper_scissors():
    cpu_input = random.randint(1, 3)
    print(f"The CPU has chosen {cpu_input}")

    if user_input == 1:
        if cpu_input == 1:
            print("Draw")

        elif cpu_input == 2:
            print("CPU wins")

        else:
            print("You win!")

    elif user_input == 2:
        if cpu_input == 1:
            print("You win!")

        elif cpu_input == 2:
            print("Draw")

        else:
            print("CPU wins")

    elif user_input == 3:
        if cpu_input == 1:
            print("CPU wins")

        elif cpu_input == 2:
            print("You win!")

        else:
            print("Draw")

gameduel = '   '

while gameduel != 'x':
     gameduel = input("Press 'r' to play , and 'x' to exit the duel \n")
     if gameduel == "r":
          rock_paper_scissors()