import turtle as turtle_module
import random

turtle_module.colormode(255)
turt = turtle_module.Turtle()
turt.speed('fastest')
turt.penup()
turt.hideturtle()
color_list = [(231, 233, 237), (236, 231, 234), (222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

turt.setheading(225)
turt.forward(300)
turt.setheading(0)
number_of_dots = 100

for dot_counter in range(1, number_of_dots + 1):
    turt.dot(20, random.choice(color_list))
    turt.forward(50)

    if dot_counter % 10 == 0:
        turt.setheading(90)
        turt.forward(50)
        turt.setheading(180)
        turt.forward(500)
        turt.setheading(0)


















screen = turtle_module.Screen()
screen.exitonclick()