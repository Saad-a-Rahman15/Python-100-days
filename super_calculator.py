def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division,
}

final = 0
num1 = float(input("Enter your first number: \n"))


def calculator():
    global num1
    calculate()

def calculate():
    global final
    for key in operations:
        print(key)
    choice_of_operation = input("Choose an operation from above: \n")
    num2 = float(input("Enter your second number: \n"))
  
    if choice_of_operation == '+':
        final = addition(num1, num2)
        print(final)

    elif choice_of_operation == '-':
        final = subtraction(num1, num2)
        print(final)

    elif choice_of_operation == '*':
        final = multiplication(num1, num2)
        print(final)

    elif choice_of_operation == '/':
        final = division(num1, num2)
        print(final)
    
user_input = '  '

calculator()

num1 = final


while True:
    user_input = input(f"Type 'y' to continue calculating with {final}, or type 'n' to start a new calculation: \n")
    if user_input == 'y':
        calculate()
    elif user_input == 'n':
        calculator()

        

    