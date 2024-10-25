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
def set_heading(num):
    angle = tim.heading()
    angle = tim.setheading(angle + num)
    return angle
num = 20
for _ in range(int(360 / num)):
    tim.color(random_color())
    tim.width(2)
    tim.circle(100)
    tim.speed("fastest")
    set_heading(num)

screen = Screen()
screen.exitonclick()