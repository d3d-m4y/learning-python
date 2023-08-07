from turtle import Turtle, Screen

import numpy as np

import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

is_race_on = False
    
guess = screen.textinput(title="Make you guess...", 
                         prompt="Which turtle will win th race? Enter a color:")

cheat = screen.textinput(title="Do you want to cheat? KEKW.",
                         prompt="Yes or No")

speed_multiplier = 1

if cheat == "yes" or cheat == "Yes" or cheat == "y":
    speed_multiplier = screen.textinput(title="Speed multiplier input: ",
                                        prompt="Enter your desired speed multiplier")
    
converted_speed_multiplier = float(speed_multiplier) + 1

print(f'You have guessed: {guess}')


def move_start(turtle, y):
    turtle.penup()
    turtle.goto(x=-225, y=y)
    turtle.pendown()
    
      
def generate_turtles(colors, turtles):
    for item in colors:
        turtle_color = item
        item = Turtle(shape="turtle")
        item.color(turtle_color)
        turtles.append(item)
        
        
def evenly_spaced_items(lower_bound, upper_bound, length):
    return np.linspace(lower_bound, upper_bound, length)
    
    
if guess:
    is_race_on = True

racers = []

generate_turtles(colors=colors, turtles=racers)
locations = evenly_spaced_items(154, -154, len(racers))

for turtle in range(len(racers)):
    move_start(racers[turtle], locations[turtle])
    
while is_race_on:
    for racer in racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_color = racer.pencolor()
            if winning_color == guess:
                print(f"You've won... nothing! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost, friggin loser... looool...")
        if racer.pencolor() == guess:
            random_distance = (random.randint(0, 10) * converted_speed_multiplier)
        else:
            random_distance = random.randint(0, 10)
        
        racer.forward(random_distance)
   

screen.exitonclick()