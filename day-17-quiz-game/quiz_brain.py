import random
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (t/f):  \n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        wrong = ["You got it wrong, your opinion is a crime, Maybe you'll find a brain back there in time",
                  "You got it wrong, I can't believe it's true, I've seen smarter things come from a zoo",
                  "You got it wrong, let's just be real, The whole class saw you miss that deal.",
                 "You got it wrong? Well that's a first, I'll just pretend my brain just burst.",
                 "You got it wrong, oh goodness, oh my, you look so funny when you try."]

        if user_ans.lower() == correct_ans.lower():
            print("You got it right!!")
            self.score += 1

        else:
            print(random.choice(wrong))
        print(f'The correct answer is {correct_ans}!')
        percentage = self.score / self.question_number
        rounded_percentage = f"{percentage:.2%}"
        print(f'Your current score is {rounded_percentage} or {self.score}/{self.question_number}.')
        print('\n')