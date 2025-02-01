x = input("Enter a number to see what prime numbers come before it!! \n")
x = int(x)
for a in range(1, x):
    is_prime = True
    c = int(a / 2)
    for b in range(2, c + 1):
        if a % b == 0 :
            is_prime = False
            break
    if is_prime == True:
        print(a)
        a += 1