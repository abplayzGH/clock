from datetime import datetime

from turtle import *
#background
# color("white")
# penup()
# goto(-200,-200)
# right(45)
# begin_fill()
# circle(400,360,4)
# end_fill()

two = Turtle()

hour = datetime.now().hour
minute = datetime.now().minute
second = datetime.now().second
hideturtle()
speed(0)
pensize(2)
penup()
goto(0,-200)
pendown()
circle(200)
penup()
goto(0,0)
pendown()

def second_hand(second):
    color("black")
    right(second*6)
    forward(175)
    backward(175)
    left(second*6)

def erase_sec(second):
    second -= 1 
    right(second*6)
    color("white")
    forward(175)
    backward(175)
    left(second*6)

def erase_min(minute):
    minute -= 1 
    right(minute*6)
    color("white")
    forward(150)
    backward(150)
    left(minute*6)


def minute_hand(minute):
    color("red")
    right(minute*6)
    forward(150)
    backward(150)
    left(minute*6)
#forever
while(True):
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    if second == 59:
        minute_hand(minute)
        erase_min(minute) 
    second_hand(second)
    erase_sec(second)


