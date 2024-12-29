import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '"', '#', '$', '%', '£', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '}', '|', '~']

print("Welcome to Saadiboy Password Generator!")
amount_of_characters = int(input("How many characters would you like in your password? \n"))
amount_of_symbols = int(input("How many symbols would you like in your password? \n"))
amount_of_numbers = int(input("How many numbers would you like in your password? \n"))
amount_of_letters = amount_of_characters - (amount_of_numbers + amount_of_symbols)

password = []

for symbol in range(1, amount_of_symbols + 1):
    password.append(random.choice(symbols))

for number in range(1, amount_of_numbers + 1):
    password.append(random.choice(numbers))

for letter in range(1, amount_of_letters + 1):
    password.append(random.choice(letters))


random.shuffle(password)

password_string = ("")
for character in password:
    password_string += character

print(f"Your password is: {password_string}")