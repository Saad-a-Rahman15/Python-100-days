from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(1080, 720)
user1_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? You are Player 1. Enter a color:  ")
print(user1_bet)
user2_bet = screen.textinput(title="Make your bet, Player 2", prompt="Which turtle will win the race? You are Player 2. Enter a color:  ")
print(user1_bet)

colors = ['red', 'orange', 'gold', 'green', 'skyblue', 'blue', 'purple']
y_positions = [-180, -130, -80, -30, 20, 70, 120]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-520, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user1_bet and user2_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 520:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user1_bet:
                print(f"Player 1, you've won! The {winning_color} turtle is the winner!")
            elif winning_color == user2_bet:
                print(f"Player 2, you've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Both of you have lost. The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()