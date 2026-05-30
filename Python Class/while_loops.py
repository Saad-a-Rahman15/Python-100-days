counter = 1
while counter < 100:
    if counter % 2 == 0 or counter % 3 == 0 or counter % 5 == 0 or counter % 7 == 0:
        print(counter)
    elif counter > 40 and counter < 60:
        continue
    counter += 1