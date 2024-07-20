from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POOL = [0, 3, 6, 9, 12, 15, 18, 21, 24]
X_POOL = [0, 3, 6, 9, 12, 15, 18, 21, 24]
STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.all_car = []

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)

            # rand_position = random.randrange(-250, 250, 20)
            # new_car.goto(310, random.randrange(-250, 250, 20))
            # new_car.setposition(300, rand_position)

            sign = 1 if random.random() < 0.5 else -1
            new_car.goto(300, random.choice(Y_POOL) * 10 * sign)
            rand_color = random.choice(COLORS)
            new_car.color(rand_color)
            self.all_car.append(new_car)

    def move_forward(self):
        for cars in self.all_car:
            cars.forward(self.car_speed)

    def level_up(self):
        self.car_speed -= MOVE_INCREMENT

