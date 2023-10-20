from datetime import datetime

from turtle import *
# background
# color("white")
# penup()
# goto(-200,-200)
# right(45)
# begin_fill()
# circle(400,360,4)
# end_fill()
# tracer(0,0)
def main():
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
    tracer(0,0)
    color("black")
    right(second*6)
    forward(175)
    backward(175)
    left(second*6)
    update()



def minute_hand(minute):
    tracer(0,0)
    color("red")
    right(minute*6)
    forward(150)
    backward(150)
    left(minute*6)
    update()
#forever
while(True):
    second 
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    main()
    minute_hand(minute - 15)
    if  second ==
    second_hand(second - 15)
    print(datetime.now().second)
    clear()
    
