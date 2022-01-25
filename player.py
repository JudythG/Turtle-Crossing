from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape):
        super().__init__(shape)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def reset(self):
        self.goto(STARTING_POSITION)

    def cross(self):
        self.forward(MOVE_DISTANCE)

    def crossed_finish(self):
        return self.ycor() > FINISH_LINE_Y

