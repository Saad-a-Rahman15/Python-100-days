from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor('grey14')
screen.setup(800, 600)
screen.title('Pong')

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()

root.resizable(False, False)

ball = Ball()
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

speed = 0.1

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(speed)
    print(speed)

    if scoreboard.l_score or scoreboard.r_score:
        if speed <= 0.026:
            speed = 0.026


    if ball.ycor() >= 275 or ball.ycor() <= -275:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() >= 330 or ball.distance(l_paddle) < 60 and ball.xcor() <= -330:
        ball.bounce_x()

    if ball.xcor() >= 400:
        ball.reset()
        scoreboard.l_point()
        speed -= 0.003

    if ball.xcor() <= -400:
        ball.reset()
        scoreboard.r_point()
        speed -= 0.003


screen.exitonclick()
