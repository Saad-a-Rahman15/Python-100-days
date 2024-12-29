question = int(input("Enter a number to see if it is a prime number! \n"))

is_prime = True


for num in range(1, question):

    if num > question / 2:
        break
    
    if question % num == 0:
        is_prime = False
        break


if is_prime == False:
    print("This isn't a prime number!!!")

else:
    print("This is a prime number!!!")