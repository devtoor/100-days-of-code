from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position[0], position[1])

    def move_up(self):
        if self.ycor() < 240:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -240:
            self.backward(20)
