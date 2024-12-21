question =input("Choose a number! \n")

question = int(question)

for answer in range(1, question):
    if answer > question / 2:
        break
    else:
        if question % answer == 0:
            print(answer)
            
print(question)
        