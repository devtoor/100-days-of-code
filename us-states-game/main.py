import turtle

import pandas

BG_IMG = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(BG_IMG)
turtle.shape(BG_IMG)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

guessed_states = []
while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                  prompt="What's another state's name?").title()
    if user_input == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break
    if user_input in all_states:
        guessed_states.append(user_input)
        state_data = data[data.state == user_input]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(user_input)
