import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def cross(t):
    turtle.forward()


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)
screen.listen()

turtle = Player(shape="turtle")
screen.onkey(fun=turtle.cross, key="Up")

car_manager = CarManager(SCREEN_WIDTH, SCREEN_HEIGHT)
scoreboard = Scoreboard()
scoreboard.display_score()

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.control_cars()
    if turtle.crossed_finish():
        turtle.reset()
        scoreboard.level_up()
        car_manager.move_faster()
    elif car_manager.detect_collision(turtle):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()

