number = int(input('Enter a number to see if what prime numbers go before it!!! \n'))


for i in range(2, number + 1):
    prime = True
    if i < 4:
        print(i)
        continue
    a = int(i/2)
    for j in range(2, a + 1):


        if i % j == 0:
            prime = False
            break


    if prime == True:
        print(i)