import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True


def exit_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(exit_game, "x")

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 325
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -325
    ):
        ball.x_bounce()

    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.increase_l_score()

    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.increase_r_score()

    screen.update()

screen.exitonclick()
