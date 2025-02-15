g = int(input("Choose a number to show its number pyramid! \n"))

for h in range(1, g):
    print(' ')
    for i in range(0, g - h):
        print("  ", end="")
    for j in range(1, h + 1):
        print(j, end=' ')