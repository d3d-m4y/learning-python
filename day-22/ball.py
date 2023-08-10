from turtle import Turtle


class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.x_move = 20
        self.y_move = 20

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
