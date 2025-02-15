p = int(input("Choose a number to show its number pyramid! \n"))

for r in range(p, 0, -1):
    print('')
    for s in range(0, r):
        print(r , end=' ')