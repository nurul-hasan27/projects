import turtle
from turtle import Turtle


class ScoreBoard:
    def __init__(self, score):
        # timmy = Turtle()
        self.score = score
        with open("data.txt") as file:
            # since the file store the data in string formate it is necessary to typecast it to int
            self.highscore = int(file.read())
        turtle.color("yellow")
        turtle.hideturtle()
        turtle.penup()
        # self.change_score(self.score, self.highscore)

    def change_score(self):
        turtle.clear()
        turtle.goto(x=0, y=300)
        turtle.write(arg=f"score : {self.score} High score : {self.highscore} ", move=False, align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        turtle.clear()
        turtle.goto(x=0, y=30)
        turtle.write(arg=f"your score : {self.score} ", move=False, align="center", font=("Courier", 24, "normal"))
        turtle.goto(x=0, y=0)
        turtle.color("red")
        turtle.write(arg=f"Game Over", move=False, align="center", font=("Courier", 30, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                # the file holds only string values... so type casting int to string values
                file.write(f"{self.highscore}")
        self.score = 0
