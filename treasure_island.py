print('''*******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     '"=.|                  |
    |___________________|__"=._o'"-._        '"=.______________|___________________
              |                '"=._o'"=._      _'"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
              |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
     _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
    |                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
    |___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************''')
while True:

    print("Welcome to Treasure Island!")
    print("I have a secret for you.")
    print("There is some treasure on this island, and if you can collect it, I will make you my king.")
    print("So, are you up for the challenge?")
    challenge = input("Press Y if you accept the challenge to be king and N for no if you decline it. \n")

    challenge = challenge.lower()

    if challenge == "y":
        direction = input("Which direction will you go? Left or right? \n")
        direction = direction.lower()
        if direction == "right":
            print("You fell into lava, you should have never accepted the challenge in the first place...")
        elif direction == "left":
            print("You are now standing in front of a lake, will you build a boat with the wood nearby, or will you swim over? \n")
            lake_crossing = input("Type 'build' for making a boat and 'swim' for swimming over.")
            lake_crossing = lake_crossing.lower()
            if lake_crossing == "swim":
                print("You were eaten by a sea monster. WOMP WOMP WOMP WOMP")
            elif lake_crossing == "build":
                print("Well done! You have crossed the lake.")
                mystery_doors = input("There are 3 doors, White , Black and Rainbow. Choose one of these colours to choose the correct door to get the treasure")
                mystery_doors = mystery_doors.lower()
                if mystery_doors == "White":
                    print("White door is jail. After 50 years, you will decay. Game Over :( ")
                elif mystery_doors == "rainbow":
                    print("You work for a pencil factory for the rest of your life, WOMP WOMP WOMP WOMP")
                elif mystery_doors == "black":
                    print("You found the treasure! Now will you give it to me, or will you run away from the Island?")
                    treasure = input("Type 'Give' to give it to me or 'Run' to leave the Treasure Island with the treasure.")
                    treasure = treasure.lower()
                    if treasure == "give":
                        print("Yes, now I have the treasure, I can rule the world!")
                        print("Thank you peasant, you have served me well, BUT GOODBYE!!!")
                        print("You Died, Game Over")
                    elif treasure == "run":
                        print("You survived, now you are the richest in the world!!!")
    quit = input("Do you want to play again? Y/N ")
    if (quit.lower().startswith('n')):
        break
    else:
        print("................................................................................................................................................................")