from turtle import Turtle

VEL = 20


class PlayerBar(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=0.7, stretch_len=5)
        self.penup()
        self.goto(position)

    def move_left(self):
        new_x = self.xcor() - VEL
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + VEL
        self.goto(new_x, self.ycor())
