from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.color('aquamarine')
        self.shape('square')
        self.shapesize(5, 1)
        self.penup()
        self.goto(pos)
        
    def up(self):
        if self.ycor() >= 230:
            return
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() <= -230:
            return
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




