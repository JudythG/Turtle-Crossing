from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.goto(x=-280, y=280)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER")

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}")

    def level_up(self):
        self.level += 1
        self.display_score()
