x = 1

b = "Outside Loop"
d = 'Inside Loop'

for a in range(x, 11):
    a = str(a)
    print(b + ' ' + a)
    for c in range(x, 6):
        c = str(c)
        print(d + ' ' + c)