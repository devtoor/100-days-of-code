import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = self.Car()
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            if car.xcor() > -340:
                car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    class Car(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("square")
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.penup()
            self.setheading(180)
            self.color(random.choice(COLORS))
            random_y = random.randint(-240, 240)
            self.goto(300, random_y)
