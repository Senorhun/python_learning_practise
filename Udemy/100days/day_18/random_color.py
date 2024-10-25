from turtle import Turtle, Screen
from random import choice, randint
import turtle
tim = Turtle()
turtle.colormode(255)
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r,g,b

directions = [0, 90, 180, 270]
for _ in range(100):
    tim.color(random_color())
    tim.setheading(choice(directions))
    tim.width(10)
    tim.forward(30)
    tim.speed(3)

screen = Screen()
screen.exitonclick()