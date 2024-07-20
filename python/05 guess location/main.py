#  issue i face in making
# 1. loop is not working properly
# 2. the repeative score board issue
#  3. how to check the user input is present in the guessed list.
import turtle
from turtle import Screen, Turtle
import pandas

my_screen = Screen()
my_turtle = Turtle()
image = "blank_states_img.gif"
my_screen.addshape(image)
# turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
my_turtle.shape(image)

text_turtle = Turtle()
data = pandas.read_csv("50_states.csv")
data_states = data.state
# print(data_states)
count = 0
guessed_stated = []
game_is_on = True
while game_is_on:
    user_input = my_screen.textinput(title=f"{count}/50 Guess the state",
                                     prompt="What 's the state name in your mind?").lower()
    for answer_state in data_states:
        if user_input == answer_state.lower():
            if answer_state.lower() not in guessed_stated:
                text_turtle.penup()
                # text_turtle.goto(x=data[data.state == state].x[0], y=data[data.state == state].y[0])
                state_data = data[data.state == answer_state]
                # this is because the data is extracted in string formate.
                text_turtle.goto(x=int(state_data.x), y=int(state_data.y))
                # text_turtle.write(arg=answer_state, align="center", font=("Courier", 10, "normal"))
                # turtle.write(answer_state)
                text_turtle.write(state_data.state.item())
                guessed_stated.append(answer_state.lower())
                count += 1
        elif user_input == "exit":
            game_is_on = False
            rest_states = []
            for rest in data_states:
                if rest.lower() not in guessed_stated:
                    rest_states.append(rest)

            rest = pandas.DataFrame(rest_states)
            rest.to_csv("missed stated.csv")
