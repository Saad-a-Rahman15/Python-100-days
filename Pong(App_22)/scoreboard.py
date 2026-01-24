from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('grey90')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 100)
        self.write(self.l_score, align='center', font=('Comic Sans MS', 80, 'normal'))
        self.goto(100, 100)
        self.write(self.r_score, align='center', font=('Comic Sans MS', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
