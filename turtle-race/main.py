import random
from turtle import Screen
from turtle import Turtle

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Enter a color ('red', 'green', 'blue'): ",
)
colors = ["red", "green", "blue"]
y_positions = [50, 0, -50]
turtles = []

for index in range(len(colors)):
    tim = Turtle("turtle")
    tim.color(colors[index])
    tim.penup()
    tim.setpos(-230, y_positions[index])
    turtles.append(tim)

is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 5))
        if turtle.xcor() > 220:
            winning = turtle.pencolor()
            if user_bet == winning:
                print(f"{winning.title()} turtle win: You win!")
            else:
                print(f"{winning.title()} turtle win: You lose!")
            is_race_on = False

screen.exitonclick()
