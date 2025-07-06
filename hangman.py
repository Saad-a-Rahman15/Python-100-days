import random

print("Welcome to Hangman!")
print("To win, you must guess all the letters to free our friend Hank, or he will be hanged!")
print("You have 8 tries.")

word_list = ["python", "coding", "javascript"]

chosen_word =  random.choice(word_list)

print(chosen_word)

for attempts in chosen_word:
    guess = input("Guess a letter: \n")
    guess = guess.lower()
    for letter in chosen_word:
        position = chosen_word.find(guess)
     
        if letter == guess:
            print("Right")
        else:
            print("Wrong")