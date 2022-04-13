from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True


def exit_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(exit_game, "x")

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move_forward()

    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        food.refresh()
        snake.reset()

    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset_score()
            food.refresh()
            snake.reset()

screen.exitonclick()
