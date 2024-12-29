x = 0
y = 1

print(x)
print(y)

for num in range(1, 101):
    z = x + y
    x = y
    y = z
    print(z)
        