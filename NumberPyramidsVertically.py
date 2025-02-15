a = int(input("Choose a number to show its number pyramid! \n"))

for x in range(1, a):
    print('')
    for y in range(1, x + 1):
        print(y, end=' ')