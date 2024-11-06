from turtle import Turtle
from food import Food

STARTING_POSITIONS = [(0,0),(-10,0),(-20,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT= 0
class Snake():
    def __init__(self, food):
        self.segments = []
        self.food = food
        self.create_snake()
        self.head = self.segments[0]
        self.segments[0].shape("square")

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position, "white")

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_input = self.head.heading()

    def up(self):
        if self.last_input != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.last_input != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.last_input != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.last_input != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, position, color):
        new_segment =  Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color(color)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self, color):
        self.add_segment(self.segments[-1].position(), color)
        