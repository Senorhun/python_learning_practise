
# import colorgram

# file_path = r'C:\Users\szaboptr\Python\practise\Udemy\100days\day_18\color_extraction\dot.jpeg'

# colors = colorgram.extract(file_path, 10)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as turtle_module
import random as r

color_list_1 = [(247, 247, 247), (172, 192, 64), (251, 250, 251), (57, 180, 73), (77, 77, 77)]
color_list_2 = [(26, 37, 50), (204, 163, 116), (246, 219, 174), (232, 203, 125), (48, 31, 19), (143, 93, 62), (34, 107, 154), (55, 186, 234), (9, 187, 229), (47, 25, 35)]

tim = turtle_module.Turtle()
turtle_module.colormode(255)

def one_line():
    for _ in range(5):
        tim.hideturtle()
        tim.penup()
        tim.forward(20)
        tim.dot(20, r.choice(color_list_2))
        tim.forward(20)
    
def turn():
    tim.setheading(90)
    tim.forward(40)
    tim.setheading(180)
    tim.forward(200)
    tim.setheading(0)

for _ in range(5):
    one_line()
    turn()

screen = turtle_module.Screen()
screen.exitonclick()

