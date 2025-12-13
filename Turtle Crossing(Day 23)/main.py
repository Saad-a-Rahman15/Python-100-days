import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray20")
screen.title("Crossy Road")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

def restart():
    player.go_to_start()
    scoreboard.reset()
    car_manager.reset()


screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(restart, "r")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()
    
    for car in car_manager.cars:
        if car.distance(player) <= 20:
            scoreboard.level = 1
            restart()

    if player.at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
            
screen.exitonclick()
