from datetime import datetime

import turtle
from tkinter import Tk as tk
t = turtle.Turtle()


num_list = [3,2,1,12,11,10,9,8,7,6,5,4]

def make_circle():
    t.hideturtle()
    turtle.tracer(0,0)
    t.pensize(2)
    t.penup()
    t.goto(0,-200)
    t.pendown()
    t.circle(200)
    t.penup()
    t.goto(0,0)
    for i in range(0,12,1):
        t.penup()
        t.forward(175)
        t.pendown()
        t.write(num_list[i])
        t.forward(25)
        t.penup()
        t.backward(200)
        t.left(10)
        t.penup()
        # t.goto(0,0)
    t.left(60)
    t.pendown()



def second_hand(second):
    # turtle.tracer(0,0)
    t.color("red")
    t.right(second*6)
    t.forward(170)
    t.backward(170)
    t.left(second*6)



def minute_hand(minute, second):
    # turtle.tracer(0,0)
    t.color("black")
    t.right(minute *6  + second/10)
    t.forward(150)
    t.backward(150)
    t.left(minute *6 + second/10)

def hour_hand(hour):
    # turtle.tracer(0,0)
    t.color("black")
    t.right(hour*6)
    t.forward(100)
    t.backward(100)
    t.left(hour*6)

#forever
while(True):
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    make_circle()
    minute_hand(minute - 15, second)
    second_hand(second - 15)
    hour_hand(hour - 27)
    turtle.update()
    t.clear()
    
