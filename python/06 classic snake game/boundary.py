# want to add a visible boundary for the snake.

from turtle import Turtle


class Boundary:
    def __init__(self):
        self.timmy = []

    def boundary(self):
        new_segment = Turtle(shape="square")
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shapesize(stretch_wid=30, stretch_len=0.1, outline=0)
        new_segment.color("white")
        new_segment.setposition(-300, 0)
        self.timmy.append(new_segment)

        new_segment = Turtle(shape="square")
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shapesize(stretch_wid=30, stretch_len=0.1, outline=0)
        new_segment.color("white")
        new_segment.setposition(300, 0)
        self.timmy.append(new_segment)

        new_segment = Turtle(shape="square")
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shapesize(stretch_wid=0.1, stretch_len=30, outline=0)
        new_segment.color("white")
        new_segment.setposition(0, -300)
        self.timmy.append(new_segment)

        new_segment = Turtle(shape="square")
        new_segment.speed(0)
        new_segment.penup()
        new_segment.shapesize(stretch_wid=0.1, stretch_len=30, outline=0)
        new_segment.color("white")
        new_segment.setposition(0, 300)
        self.timmy.append(new_segment)
