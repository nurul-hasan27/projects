from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()
        # this is very good approach to just call the turtle ones and  then change the position
        # I was thingking to each time create a new turtle and delete the prev one... 🥴

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setposition(random_x, random_y)

