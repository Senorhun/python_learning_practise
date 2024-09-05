import turtle
import time

# window

window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("PONG")
window.tracer(0)


# left player
left_player = turtle.Turtle()
left_player.speed(0)
left_player.shape("square")
left_player.shapesize(stretch_wid=5, stretch_len=1)
left_player.color("red")
left_player.penup()
left_player.goto(-350, 0)

# right player
right_player = turtle.Turtle()
right_player.speed(0)
right_player.shape("square")
right_player.shapesize(stretch_wid=5, stretch_len=1)
right_player.color("blue")
right_player.penup()
right_player.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

#setting the "speed" of ball
ball.changeX = 0.3
ball.changeY = -0.3

#score
right_player_score = 0
left_player_score  = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write(f"Red player: {left_player_score}          Blue player: {right_player_score}", align="center", font=("Curier",24, "normal"))

def left_player_up():
    y = left_player.ycor()
    y += 30
    left_player.sety(y)


def left_player_down():
    y = left_player.ycor()
    y -= 30
    left_player.sety(y)


def right_player_up():
    y = right_player.ycor()
    y += 30
    right_player.sety(y)


def right_player_down():
    y = right_player.ycor()
    y -= 30
    right_player.sety(y)


window.onkey(left_player_up, "w")
window.onkey(left_player_down, "s")
window.onkey(right_player_up, "Up")
window.onkey(right_player_down, "Down")
window.listen()


while True:
    # updating screen
    window.update()

    time.sleep(0.0001) #slowing the ball

    ball.setx(ball.xcor() + ball.changeX)
    ball.sety(ball.ycor() + ball.changeY)

    # bouncing from top
    if ball.ycor() > 288:  # have to calculate shape of the ball
        ball.sety(288)
        ball.changeY *= -1
    # bouncing from bottom
    if ball.ycor() < -288:  # have to calculate shape of the ball
        ball.sety(-288)
        ball.changeY *= -1
    # touch right side
    if ball.xcor() > 388:
        ball.goto(0, 0)
        ball.changeX *= -1
        left_player_score += 1
        score.clear()
        score.write(f"Red player: {left_player_score}          Blue player: {right_player_score}", align="center", font=("Curier",24, "normal"))
        window.update()
        time.sleep(1.5)


    # touch left side
    if ball.xcor() < -388:
        ball.goto(0, 0)
        ball.changeX *= -1
        right_player_score += 1
        score.clear()
        score.write(f"Red player: {left_player_score}          Blue player: {right_player_score}", align="center", font=("Curier",24, "normal"))
        window.update()
        time.sleep(1.5)

    if right_player.xcor() - 20 < ball.xcor() < right_player.xcor() and right_player.ycor() - 40 < ball.ycor() < right_player.ycor() + 40:
        ball.setx(right_player.xcor() - 20)
        ball.changeX *= -1

    if left_player.xcor() + 20 > ball.xcor() > left_player.xcor() and left_player.ycor() - 40 < ball.ycor() < left_player.ycor() + 40:
        ball.setx(left_player.xcor() + 20)
        ball.changeX *= -1
    

"""
teki = turtle.Turtle()
teki.speed(1)
teki.shape("turtle")
teki.color("purple")
teki.shapesize(stretch_wid=5, stretch_len=1)
teki.penup()
teki.forward(200)
teki.right(90)
teki.forward(200)
teki.right(90)
teki.forward(200)
teki.right(90)
teki.forward(200)
teki.right(90)
"""
