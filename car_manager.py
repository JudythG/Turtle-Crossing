from turtle import Turtle
from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_WIDTH = 20


class CarManager:
    def __init__(self, width, height):
        self.cars = []
        self.x_start = width / 2 + 15   # start just off-screen
        self.y_max = int((height / 2) - (2 * LANE_WIDTH))
        self.move_speed = 0.1

    def drive(self):
        """ move all the card forward """
        for car in self.cars:
            car.move(MOVE_INCREMENT)

    def control_cars(self):
        """ function called outside this class. It adds, drives, and removes cars """
        self.add_cars()
        self.remove_cars()
        self.drive()

    def add_cars(self):
        """ add cars at random times in random locations """
        make_car = random.randint(0, 7)
        if make_car == 0:
            y_start = random.randint(-self.y_max+LANE_WIDTH, self.y_max)
            car = Car(random.choice(COLORS))
            car.goto(x=self.x_start, y=y_start)
            self.cars.append(car)

    def remove_cars(self):
        """" Remove cars once they've driven off-screen """
        for car in self.cars:
            # print(car.xcor())
            if car.xcor() <= -self.x_start-20:
                self.cars.remove(car)
                # print("Removed car")

    def move_faster(self):
        self.move_speed *= 0.9

    # ToDo: store car lane (y-coord) in a dictionary so can search for car in the same lane as the turtle
    #  rather than checking all
    def detect_collision(self, t):
        for car in self.cars:
            if car.distance(t) < 15:
                return True
        return False




