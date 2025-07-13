import random

word_list = ['saad', 'door', 'hide']

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ''
for position in range(0, len(chosen_word)):
    placeholder += '_'
print(placeholder)

game_over = False

correct_letters = []

while not game_over:

    guessed_word = ''

    guess = input("Guess a letter: \n")

    for letter in chosen_word:
        if letter == guess:
            guessed_word += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            guessed_word += letter
        else:
            guessed_word += '_'


    print(guessed_word)