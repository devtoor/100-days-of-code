import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-14, 14) * 20
        rand_y = random.randint(-14, 14) * 20
        self.goto(rand_x, rand_y)
