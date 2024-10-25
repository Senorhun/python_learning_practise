from turtle import Turtle, Screen
from random import choice
tim = Turtle()
num_of_side_1 = 5
num_of_side_2 = 5

# for _ in range(num_of_side_1):
#     if num_of_side_1 == 4:
#         tim.forward(100)
#         tim.right(90)
#     elif num_of_side_1 == 5:
#         tim.forward(100)
#         tim.right(72)

# for _ in range(num_of_side_1):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(num_of_side_2):
#     tim.forward(100)
#     tim.right(72)
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def draw_shape(num_side):
    angle = 360 / num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)
for _ in range(3,11):
    tim.color(choice(colors))
    draw_shape(_)
screen = Screen()
screen.exitonclick()