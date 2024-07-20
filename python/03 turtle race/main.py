import random
from turtle import Turtle, Screen
my_screen = Screen()
my_screen.setup(width=550, height=450)
my_screen.screensize(canvwidth=500, canvheight=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win?, Enter the colour : ")
colour = ["red", "orange", "yellow", "green", "blue", "purple"]
timmy = ["t1", "t2", "t3", "t4", "t5", "t6"]
y_position = [-70, -40, -10, 20, 50, 80]

for i in range(0, 6):
    timmy[i] = Turtle(shape="turtle")
    timmy[i].color(colour[i])
    timmy[i].penup()
    timmy[i].goto(x=-230, y=-100 + (40 * i))

is_race_on = True
while is_race_on:
    for tim_turtle in timmy:
        rand_distance = random.randint(0, 10)
        tim_turtle.forward(rand_distance)
        if tim_turtle.xcor() > 230:
            is_race_on = False
            winning_color = tim_turtle.pencolor()
            if user_bet == winning_color:
                print("your prediction was right! you win!!🥳")
            else:
                print(f"you were wrong,{winning_color} turtle win.. you loose🙁")

my_screen.exitonclick()

