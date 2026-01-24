from turtle import Turtle

FONT = ("Comic Sans MS", 25, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("gold1")
        self.goto(-280, 250)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        # self.goto(0, 0)
        self.level = 1
        # self.color("red")


    def reset(self):
        self.level = 1
        self.update_score()
        
