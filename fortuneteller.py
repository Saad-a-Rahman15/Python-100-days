import random

print('<fortuneteller> I am the fortune teller')
print('<Some guy beside him> sure')

points = 0
question_amount = 5
random_answer = ['Yes', 'no', "I don't care"]
random_result = ['You have a good future', 'You are absolutely doomed like you can"t do anything in life', 'Womp Womp i wont tell u']


for i in range(question_amount):
    questions = input(f"<fortuneteller> Ask your  question. You have {question_amount} questions left. \n")
    his_answer = random.choice(random_answer)
    print(his_answer)
    question_amount -= 1

    if his_answer == random_answer[0]:
        points += 3
    if his_answer == random_answer[1]:
        points += 1
    if his_answer == random_answer[2]:
        points += 2

print(f'You got {points} points.')

print(random.choice(random_result))



