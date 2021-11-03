from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("Courier", 50, "normal"))

    def reset_score(self):
        self.score = 0
