import turtle
import pandas

from state import State

screen = turtle.Screen()
screen.title("U.S. State Game")

# Adding the US map as a shape for turtle instances
us_map_image = "blank_states_img.gif"
screen.addshape(us_map_image)

# Change the screen background to the US map using turtle instance
turtle.shape(us_map_image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guessed States",
                                    prompt="Give another state's name").title()
    if answer_state == "Exit":
        # Create states_to_learn.csv file containing all the states not found
        states_to_learn = pandas.DataFrame(list(set(all_states) - set(guessed_states)))
        states_to_learn.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        # Adding correct guess to guessed_states
        guessed_states.append(answer_state)
        # Retrieve coordinates(x, y)
        state_data = data[data.state == answer_state]
        # Create a turtle
        state = State(answer_state, state_data.x, state_data.y)




turtle.mainloop()