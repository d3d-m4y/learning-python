from turtle import Screen
from paddle import Paddle
from ball import Ball

import time

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ghetto Pong")
screen.tracer(0)

p1_paddle = Paddle("p1")
p2_paddle = Paddle("p2")
ball = Ball()

game_running = True

# game loop
while game_running:
    screen.update()
    time.sleep(0.15)

    screen.listen()
    screen.onkey(key="w", fun=p1_paddle.move_up)
    screen.onkey(key="s", fun=p1_paddle.move_down)
    
    ball.move()
    
    # wall collision detection
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
        
    # player 1 paddle collision detection
    if ball.distance(p1_paddle) < 50 and ball.xcor() > 330:
        ball.paddle_bounce()
        
    # player 2 paddle collision detection
    if ball.distance(p2_paddle) < 50 and ball.xcor() > -330:
        ball.paddle_bounce()
    
# required to keep the screen up until a click is received
screen.exitonclick()
