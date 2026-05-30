print("Welcome to Rock Paper Scissors! Choose your options now!")

player1 = input("Player1, choose from: 'r' for Rock | 'p' for Paper | 's' for Scissors \n")
player2 = input("Player2, choose from: 'r' for Rock | 'p' for Paper | 's' for Scissors \n")

if player1 == player2:
    print("Its a draw!!")
elif player1 == "r" and player2 == "s":
    print("Player 1 wins!!")
elif player1 == "p" and player2 == "s":
    print("Player 2 wins!!")
elif player1 == "p" and player2 == "r":
    print("Player 1 wins!!")
elif (player1 != "r" or "s" or "p") and (player2 != "r" or "s" or "p"):
    print("That didn't work :(")

else:
    print("Player 2 wins!!")