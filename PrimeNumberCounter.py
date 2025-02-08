total_prime_numbers = int(input("How many prime numbers do you want? \n"))

counter = 0
for x in range(1, 1000000):
    prime = True
    for y in range(2, x):
        if x % y == 0:
            prime = False
            break
    if prime == True:
        if counter < total_prime_numbers:
            print(x)
            counter += 1
