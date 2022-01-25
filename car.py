from turtle import Turtle

STRETCH_WIDTH = 2


class Car(Turtle):
    def __init__(self, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=STRETCH_WIDTH)
        self.setheading(180)
        self.color(color)
        self.penup()

    def move(self, distance):
        self.forward(distance)
