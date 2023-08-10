from turtle import Turtle


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("circle")

    def move(self):
        self.setheading(33.75)
        self.forward(20)
