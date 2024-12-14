print("Welcome to the Saadiboy Pass Super Calculator!!")
print("You have been accepted to use this special calculator!")
print("Let's Start!")

question = input("Press 1 for addition, 2 for subtraction, 3 for multipication, and 4 for division! \n")


x = input("Choose your first number!\n")
x = int(x)

y = input("Choose your second number!\n")
y = int(y)


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multipy(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("That's not going to work, I'm afraid.")
        print("But.....")
        return
    return x / y

if question == '1':
    print('Your answer is ' + str(add(x, y)) + '!')
elif question == '2':
    print('Your answer is ' + str(subtract(x, y)) + '!')
elif question == '3':
    print('Your answer is ' + str(multipy(x, y)) + '!')
elif question == '4':
    print('Your answer is ' + str(divide(x, y)) + '!')