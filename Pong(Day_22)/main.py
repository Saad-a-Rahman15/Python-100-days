from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor('grey14')
screen.setup(800, 600)
screen.title('Pong')

ball = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    if ball.ycor() >= 275 or ball.ycor() <= -275:
        ball.bounce()


screen.exitonclick()
