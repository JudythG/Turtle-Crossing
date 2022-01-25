from turtle import Turtle
from car import Car
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LANE_WIDTH = 20
CAR_LANE_START = 250
COLLISION_DISTANCE = 20


class CarManager:
    def __init__(self, width, height):
        self.cars = []
        self.x_start = width / 2 + 15   # start just off-screen
        self.move_distance = MOVE_INCREMENT

    def drive(self):
        """ move all the card forward """
        for car in self.cars:
            car.move(self.move_distance)

    def control_cars(self):
        """ function called outside this class. It adds, drives, and removes cars """
        self.add_cars()
        self.remove_cars()
        self.drive()

    def add_cars(self):
        """ add cars at random times in random locations """
        make_car = random.randint(0, 7)
        if make_car == 0:
            # y_start = random.randint(-self.y_max+LANE_WIDTH, self.y_max)
            y_start = random.randint(-CAR_LANE_START, CAR_LANE_START)
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
        self.move_distance += MOVE_INCREMENT

    def detect_collision(self, t):
        for car in self.cars:
            if car.distance(t) < COLLISION_DISTANCE:
                return True
        return False




