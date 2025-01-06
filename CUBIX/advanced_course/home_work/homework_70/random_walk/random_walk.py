from turtle import Turtle, Screen
from random import choice
tim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
for _ in range(100):
    tim.color(choice(colors))
    tim.setheading(choice(directions))
    tim.width(10)
    tim.forward(30)
    tim.speed(10)


screen = Screen()
screen.exitonclick()