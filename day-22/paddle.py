from turtle import Turtle

HEIGHT = 5  # 5 * 20px = 100px
WIDTH = 1   # 1 * 20px = 20px, not really needed - default is 20px

P1_INITIAL_X = 350
P2_INITIAL_X = -360
INITIAL_Y = 0


class Paddle(Turtle):

    def __init__(self, player) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=WIDTH, stretch_wid=HEIGHT)

        if player == "p1":
            self.goto(x=P1_INITIAL_X, y=INITIAL_Y)
        else:
            self.goto(x=P2_INITIAL_X, y=INITIAL_Y)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
