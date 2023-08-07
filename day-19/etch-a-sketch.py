from turtle import Turtle, Screen

etch = Turtle()


def move_forward():
    etch.forward(10)


def turn_left():
    etch.left(15)
    

def move_backward():
    etch.backward(10)
    

def turn_right():
    etch.right(15)


screen = Screen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.exitonclick()