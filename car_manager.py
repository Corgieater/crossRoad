from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def make_car(self):
        rand = random.randint(1, 6)
        if rand == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_len=1.5)
            new_car.color(random.choice(COLORS))
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
