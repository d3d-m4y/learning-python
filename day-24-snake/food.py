from turtle import Turtle

import random


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # generate a random position for the food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
