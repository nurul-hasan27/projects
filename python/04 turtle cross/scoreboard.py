from turtle import Turtle
FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier",35 , "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-230, 270)
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 40)
        self.write(f"Final Score : {self.level}", align="center", font=FONT)
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over", align="center", font=GAME_OVER_FONT)

