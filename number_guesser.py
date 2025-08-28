import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number from 1 to 100")

i = random.randint(1, 100)

POINTS = 0
tries = 0

def easy_mode():
    global POINTS
    global tries
    POINTS = 10
    for a in range(POINTS):
        tries = int(input("Guess a number: \n"))
        if tries < i:
            print("Too Low")
        elif tries > i:
            print("Too High")
        elif tries == i:
            print("You Win")
            return


def hard_mode():
    global POINTS
    global tries
    POINTS = 5
    for a in range(POINTS):
        tries = int(input("Guess a number: \n"))
        if tries < i:
            print("Too Low")
        elif tries > i:
            print("Too High")
        elif tries == i:
            print("You Win")
            return

mode = input("Choose a difficulty: enter 'e' for easy mode, and 'h' for hard mode. \n")

if mode == 'e':
    easy_mode()
elif mode == 'h':
    hard_mode()
else:
    print("That didn't work")