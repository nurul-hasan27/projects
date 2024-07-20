# snake brain

from turtle import Turtle
STARTING_POSITION = [(-20, 0), (-40, 0)]  # the position tuple
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.new_segment = Turtle(shape="square")
        self.new_segment.speed(0)
        self.new_segment.penup()
        self.new_segment.shapesize(stretch_wid=1, stretch_len=1, outline=5)
        self.new_segment.color("white")
        self.new_segment.goto(0, 0)
        self.segment.append(self.new_segment)
        self.head = self.segment[0]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.speed(0)
            new_segment.penup()
            new_segment.shapesize(stretch_wid=0.8, stretch_len=0.8, outline=1)
            new_segment.color("white")
            new_segment.goto(position)
            self.segment.append(new_segment)

    def extend_snake(self):
        new_segment = Turtle(shape="square")
        new_segment.speed(0)
        new_segment.penup()
        new_segment.color("white")
        new_segment.shapesize(stretch_wid=0.8, stretch_len=0.8, outline=1)
        new_segment.goto(self.segment[-1].position())
        self.segment.append(new_segment)

    def body_collision(self):
        # for seg in self.segment:
        #     if seg == self.head:
        #         pass
        #     elif self.head.distance(seg) < 10:
        #         return True

        # using slicing
        for seg in self.segment[1:]:
            if self.head.distance(seg) < 10:
                return True

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def up(self):
        # new_heading = self.segment[0].heading() + 90
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # new_heading = self.segment[0].heading() + 90
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # these above lines are not useful coz these change the arrow head acc to the direction of current position
    # the lower one directly assign the direction angle
    def left(self):
        # new_heading = self.segment[0].heading() -180
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # new_heading = self.segment[0].heading() + 0
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        #  this send the turtle of the snake to off the screen
        #  this is to solve the issue.. that we can't delete a turtle once it is created.
        for seg in self.segment:
            seg.goto(1000, 100)
        self.segment.clear()

        self.new_segment.shapesize(stretch_wid=1, stretch_len=1, outline=5)
        self.new_segment.color("white")
        self.new_segment.goto(0, 0)
        self.segment.append(self.new_segment)
        self.create_snake()
        self.head = self.segment[0]
