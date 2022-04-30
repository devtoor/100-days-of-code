from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Courier", 52, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 280)
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.show_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(f"{self.high_score}"))
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            False,
            ALIGNMENT,
            SCORE_FONT,
        )
