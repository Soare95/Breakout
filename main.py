from turtle import Screen
from bar import PlayerBar
from ball import Ball
from enemy import EnemyBar
from scoreboard import Scoreboard

WIDTH, HEIGHT = 500, 600
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Breakout Game")
screen.bgcolor("black")
screen.tracer(0)


bar = PlayerBar((0, -220))
ball = Ball()
enemy_bars = EnemyBar()
score_board = Scoreboard()
enemy_bars.create_enemy_bars()

screen.listen()
screen.onkey(key="Left", fun=bar.move_left)
screen.onkey(key="Right", fun=bar.move_right)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect Game over
    if ball.ycor() < -280:
        game_is_on = False
        score_board.clear()
        score_board.write(f"Game Over! You scored {score_board.score}", align="center", font=("Courier", 24, "normal"))
        screen.update()

    # Detect collision with top wall
    if ball.ycor() > 290:
        ball.bounce_y()

    # Detect collision with left and right walls
    if ball.xcor() > 230 or ball.xcor() < -240:
        ball.bounce_x()

    # Detect collision with the paddle
    if ball.distance(bar) < 35 and ball.ycor() > -260:
        ball.bounce_y()

    # Detect collision with enemy bars
    for enemy_bar in enemy_bars.all_bars:
        if ball.distance(enemy_bar) < 20:
            score_board.increase_score()
            ball.bounce_y()
            enemy_bar.goto(1000, 1000)


screen.exitonclick()
