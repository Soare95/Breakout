from turtle import Turtle


class EnemyBar(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bars = []

    def create_enemy_bars(self):
        x_axis = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
        y_axis = [270, 250, 230, 210, 190]
        for bar_index_row in range(9):
            for bar_index_column in range(5):
                self.new_bar = Turtle()
                self.new_bar.penup()
                self.new_bar.shape("square")
                self.new_bar.color("yellow")
                self.new_bar.turtlesize(stretch_wid=0.4, stretch_len=2)
                self.all_bars.append(self.new_bar)
                self.new_bar.goto(x=x_axis[bar_index_row], y=y_axis[bar_index_column])