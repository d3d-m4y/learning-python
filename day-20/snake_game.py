from turtle import Screen, Turtle
from snake import Snake

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake.")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)
    
game_running = True

while game_running:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

screen.exitonclick()