name = (input("Enter your name: \n"))



print(">>> Normal While Loop >>>")

a = 1

while a < 6:
    print(name + str(a))
    a += 1



print(">>> Break While Loop >>>")

b = 1

while b < 100:
    if b % 17 == 0:
            break
    print(b)
    b += 1

print(">>> Continue While Loop >>>")

c = 1

while c < 20:
    c += 1
    if c % 3 == 0:
        continue
    print(c)