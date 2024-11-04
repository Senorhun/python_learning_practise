from random import randint
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.penup()
tim.color("red")

tom = Turtle()
tom.shape("turtle")
tom.penup()
tom.color("blue")

tam = Turtle()
tam.shape("turtle")
tam.penup()
tam.color("green")

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Select a turtle to bet on!")

tim.goto(x=-230, y= 0)
tom.goto(x=-230, y= 100)
tam.goto(x=-230, y= -100)
turtles = [tim,tom,tam]


def racing():
    if user_bet:
        is_race_on = True
    while is_race_on:
        tim.forward(randint(1,5))
        tom.forward(randint(1,5))
        tam.forward(randint(1,5))
        winner = None
        if tim.xcor() > 230 or tom.xcor() > 230 or tam.xcor() > 230:
            is_race_on = False
            if tim.xcor() > 230:
                winner = tim.color()
            elif tom.xcor() > 230:
                winner = tom.color()
            elif tam.xcor() > 230:
                winner = tam.color()
    print(f"Yaay!! {winner[0]} turtle won the race!")
    if user_bet == winner[0]:
        print("And you won the bet!")
    else:
        print("So you lost the bet...")

racing()
screen.exitonclick()