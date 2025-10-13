from turtle import Turtle, Screen

tortoise = Turtle()
screen = Screen()
tortoise.shape('arrow')
tortoise.width(3)

def move_forwards():
    tortoise.forward(10)

def move_backwards():
    tortoise.backward(10)

def turn_right():
    tortoise.right(10)

def turn_left():
    tortoise.left(10)

def turn_red():
    tortoise.color('red')

def turn_orange():
    tortoise.color('orange')

def turn_yellow():
    tortoise.color('gold')

def turn_green():
    tortoise.color('green')

def turn_blue():
    tortoise.color('blue')

def turn_purple():
    tortoise.color('magenta')

def turn_white():
    tortoise.color('white')

def turn_black():
    tortoise.color('black')

def clear_screen():
    tortoise.clear()
    tortoise.penup()
    tortoise.goto(0, 0)
    tortoise.setheading(0)
    tortoise.color('black')
    tortoise.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="r", fun=turn_red)
screen.onkey(key="o", fun=turn_orange)
screen.onkey(key="y", fun=turn_yellow)
screen.onkey(key="g", fun=turn_green)
screen.onkey(key="b", fun=turn_blue)
screen.onkey(key="p", fun=turn_purple)
screen.onkey(key="h", fun=turn_white)
screen.onkey(key="l", fun=turn_black)
screen.onkey(key="Return", fun=clear_screen)

screen.exitonclick()