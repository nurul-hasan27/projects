from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.num1 = random.randint(0, 200)
        self.num2 = random.randint(0, 200)
        self.setposition(self.num1, self.num2)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def collision(self):
        self.y_move *= -1

    def collision_x(self):
        self.x_move *= -1

