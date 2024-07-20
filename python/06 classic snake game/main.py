from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from boundary import Boundary

score = 0

score_board = ScoreBoard(score)
screen = Screen()
snake = Snake()
food = Food()
boundary = Boundary()

screen.setup(width=650, height=650)
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.title("Guddu 's snake game")
starting_position = [(0, 0), (-20, 0), (-40, 0)]  # the position tuple
segments = []
screen.tracer(0)
# boundary.boundary()

# for position in starting_position:
#     new_segment = Turtle(shape="square")
#     new_segment.speed(0)
#     new_segment.penup()
#     new_segment.color("white")
#     new_segment.goto(position)
#     segments.append(new_segment)
level = 0.3
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(level)
    score_board.change_score()

    # very first attempt to move the snake
    # for seg in segments:
    #     seg.forward(10)
    #     time.sleep(0.1)
    #     if seg.xcor() > 300:
    #         # game_is_on = False

    # using diff and optimises technique to move the snake
    # for seg_num in range(len(segments)-1, 0, -1):
    #     time.sleep(0.1)
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)

    # using OOPS
    snake.move()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.up, "W")
    screen.onkey(snake.down, "S")
    screen.onkey(snake.left, "A")
    screen.onkey(snake.right, "D")
    # collision detection with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        level -= 0.02
        score_board.score += 1
        score_board.change_score()
        snake.extend_snake()

    # Detection of the collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -315 or snake.head.ycor() > 315 or snake.head.ycor() < -310:
        choose = screen.textinput(title="wanna continue?", prompt="Enter 'continue' or else 'over' : ")
        if choose == "over":
            game_is_on = False
            score_board.reset()
            score_board.game_over()

        else:
            score_board.reset()
            snake.reset()
            level = 0.3

    # collision with body
    if snake.body_collision():
        choose = screen.textinput(title="wanna continue?", prompt="Enter 'continue' or else 'over' : ")
        if choose == "over":
            game_is_on = False
            score_board.reset()
            score_board.game_over()
        else:
            score_board.reset()
            snake.reset()
            level = 0.3

screen.exitonclick()

