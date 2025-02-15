l = int(input("Choose a number to show its number pyramid! \n"))

for m in range(l, 1, -1):
    print('')
    for n in range(1, m + 1):
        print(n, end=' ')