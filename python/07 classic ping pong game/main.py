from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
# screen.screensize(canvwidth=1400, canvheight=750)
# there is no need to write this thing

# turning animation off
screen.tracer(0)

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
screen.listen()
scoreboard = ScoreBoard()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

level = 0.1
game_is_on = True
while game_is_on:
    # this just sleep the screen for that amount of time before each update
    time.sleep(level)
    # updating the screen to show movement of paddle
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collision()
    elif ball.xcor() > 320 or ball.xcor() < -320:
        if ball.distance(l_paddle) < 50 and ball.x_move < 0:
            ball.collision_x()
            scoreboard.left_score()
        elif ball.distance(r_paddle) < 50 and ball.x_move > 0:
            ball.collision_x()
            scoreboard.right_score()
        level -= 0.005
    if ball.xcor() > 380 or ball.xcor() < -380:
        game_is_on = False
        scoreboard.game_over()
screen.exitonclick()
