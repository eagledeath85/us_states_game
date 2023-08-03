import turtle



screen = turtle.Screen()
screen.title("U.S. State Game")

# Adding the us map as a shape for turtle instances
us_map_image = "blank_states_img.gif"
screen.addshape(us_map_image)

# Change the screen background to the US map using turtle instance
turtle.shape(us_map_image)




screen.exitonclick()