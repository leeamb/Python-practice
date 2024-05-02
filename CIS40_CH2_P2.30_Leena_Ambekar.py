# CIS_CH2_P2.30
# Leena Ambekar
# This program uses turtle module to draw olympic Rings

from turtle import * #importing functions from turtle module to draw circles.

#Create a window to draw circle
setup(width=500, height=500, startx=0, starty=50)

#Give a title to the window
title("Olympic Ring Program")

#create a pen to draw
turtle = Turtle()

#preparing a pen to draw
turtle.up()

#start drawing
turtle.goto(-100,0)
turtle.down()

#assign a color to circle
turtle.color("blue")

#size of a circle.
turtle.circle(50)

####### next Circle BLACK
turtle.up()
turtle.goto(0,0)
turtle.down()
turtle.color("black")
turtle.circle(50)

####### next Circle RED
turtle.up()
turtle.goto(100,0)
turtle.down()
turtle.color("red")
turtle.circle(50)

####### next Circle YELLOW
turtle.up()
turtle.goto(-50,-75)
turtle.down()
turtle.color("yellow")
turtle.circle(50)

####### next Circle GREEN
turtle.up()
turtle.goto(50,-75)
turtle.down()
turtle.color("green")
turtle.circle(50)

done()
