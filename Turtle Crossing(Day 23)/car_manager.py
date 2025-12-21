from turtle import Turtle
import random

COLORS = lambda: random.randint(0,255)

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_car(self):
        ran_chance = random.randint(1, 6)
        if ran_chance == 1: 
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(('#%02X%02X%02X' % (COLORS(),COLORS(),COLORS())))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)
        
    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def reset(self):
        for car in self.cars:
            car.hideturtle()
        self.cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
