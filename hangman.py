import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

stages = ['''
          
  +---+
  |    |
  O    |  
 /|\\   | 
 / \\   |
       |
=========''',
'''
  +---+
  |   |
  O   | 
 /|\\  | 
 /    |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|\\  | 
      |
      |
=========''',
'''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
      |
      |
      |
      |
      |
=========''']


word_list = [
    "apple", "banana", "orange", "grape", "strawberry", "watermelon", "lemon", "lime", "mango", "peach",
    "pear", "plum", "kiwi", "pineapple", "blueberry", "raspberry", "blackberry", "cherry", "apricot", "fig",
    "date", "coconut", "papaya", "guava", "nectarine", "melon", "cantaloupe", "pomegranate", "tangerine", "passionfruit"
    "dog", "cat", "mouse", "elephant", "lion", "tiger", "bear", "zebra", "monkey", "giraffe",
    "wolf", "fox", "deer", "rabbit", "kangaroo", "koala", "panda", "rhino", "hippo", "bat",
    "eagle", "hawk", "falcon", "owl", "parrot", "penguin", "dolphin", "shark", "whale", "seal",
    "car", "truck", "plane", "train", "boat", "bicycle", "motorcycle", "scooter", "bus", "tram",
    "subway", "helicopter", "yacht", "canoe", "skateboard", "wagon", "rocket", "hovercraft", "jeep", "minivan",
    "run", "walk", "jump", "swim", "fly", "crawl", "climb", "sit", "stand", "sleep",
    "eat", "drink", "read", "write", "sing", "dance", "laugh", "cry", "talk", "listen",
    "happy", "sad", "angry", "excited", "bored", "scared", "tired", "nervous", "proud", "shy",
    "jealous", "confused", "hopeful", "grateful", "anxious", "lonely", "curious", "ashamed", "content", "frustrated",
    "big", "small", "tall", "short", "fast", "slow", "hot", "cold", "loud", "quiet",
    "new", "old", "young", "ancient", "clean", "dirty", "soft", "hard", "bright", "dark",
    "red", "blue", "yellow", "green", "orange", "purple", "pink", "brown", "black", "white",
    "gray", "beige", "cyan", "magenta", "maroon", "navy", "teal", "turquoise", "gold", "silver",
    "bread", "rice", "pasta", "cheese", "butter", "egg", "milk", "chicken", "beef", "fish",
    "pizza", "burger", "sandwich", "salad", "soup", "cake", "cookie", "icecream", "cereal", "tofu",
    "hammer", "screwdriver", "wrench", "pliers", "drill", "saw", "tape", "glue", "ladder", "nail",
    "screw", "chisel", "level", "clamp", "blade", "measuringtape", "axe", "shovel", "hoe", "rake",
    "mountain", "valley", "forest", "river", "lake", "ocean", "desert", "island", "volcano", "hill",
    "sun", "moon", "star", "cloud", "rain", "snow", "storm", "wind", "lightning", "thunder",
    "head", "eye", "ear", "nose", "mouth", "hand", "arm", "leg", "foot", "knee",
    "toe", "finger", "elbow", "shoulder", "chest", "back", "stomach", "neck", "hip", "wrist",
    "school", "hospital", "library", "office", "store", "market", "museum", "park", "zoo", "restaurant",
    "hotel", "airport", "station", "church", "temple", "mall", "stadium", "theater", "gym", "pool", "mosque"]

chosen_word = random.choice(word_list)

placeholder = ''
for position in range(0, len(chosen_word)):
    placeholder += '_'
print(f'Word to guess: {placeholder}')

game_over = False

correct_letters = []

lives = 6

guessed_letters = list()

while not game_over:
    print(f"*************************************** {lives}/6 LIVES LEFT ************************************************")

    guessed_word = ''

    guess = input("Guess a letter: \n")
    guessed_letters += guess

    joined_guessed_letters = ','.join(guessed_letters)

    print(f'You have guessed the letters: {joined_guessed_letters}')

    print(stages[lives])

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(stages[0])
            game_over = True
            print("*********************************************************************You lose.*************************************************************")
            print(f'The word was {chosen_word}')


    for letter in chosen_word:
        if letter == guess:
            guessed_word += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            guessed_word += letter
        else:
            guessed_word += '_'


    print(guessed_word)

    if "_" not in guessed_word:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^You win!^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        game_over = True