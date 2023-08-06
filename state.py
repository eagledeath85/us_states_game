from turtle import Turtle


class State(Turtle):
    """
    Class holding the attributes of a state
    """
    def __init__(self, answer_state, x_cor, y_cor):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(int(x_cor), int(y_cor))
        self.write(answer_state)
