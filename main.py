import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")

# Adding the US map as a shape for turtle instances
us_map_image = "blank_states_img.gif"
screen.addshape(us_map_image)

# Change the screen background to the US map using turtle instance
turtle.shape(us_map_image)

data = pandas.read_csv("50_states.csv")
states = data.state
answer_state = screen.textinput(title="Guess the State", prompt="Give another state's name")
for state in states:
    if answer_state.casefold() == state.casefold():
        # TODO: Find how to retrieve coordinates(x, y) with pandas
        coordinates = data[state(data.x, data.y)]
        print()



screen.exitonclick()