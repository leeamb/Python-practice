import turtle

canvas = turtle.getscreen()

t = turtle.Turtle()

canvas.title("Akshat's Indian Flag")

t.goto(-150,0)

t.fillcolor("green")

t.begin_fill()

t.forward(300)

t.left(90)

t.forward(60)

t.end_fill()

t.forward(120)

t.left(90)

t.forward(300)

t.left(90)

t.forward(180)

t.left(180)

t.fillcolor("green")

t.begin_fill()

t.forward(60)

t.right(90)

t.forward(300)

t.end_fill()

t.left(90)

t.forward(60)

t.left(90)

t.forward(300)

t.left(180)

t.forward(150)

t.left(180)

t.pen(pencolor="blue", fillcolor="white", pensize=5)

t.begin_fill()

t.circle(30)

t.end_fill()

t.pen(fillcolor="orange", pensize=1)

t.begin_fill()

t.forward(150)

t.left(270)

t.forward(60)

t.left(270)

t.forward(300)

t.left(270)

t.forward(60)

t.left(270)

t.forward(300)

t.end_fill()

t.left(180)

t.forward(150)

t.left(270)

t.pen(pencolor="blue", fillcolor="white", pensize=5)

t.begin_fill

t.forward(60)

t.penup()

t.left(90)

t.forward(30)

t.left(90)

t.forward(30)

t.left(90)

t.pendown()

t.forward(60)

t.left(270)

t.penup()

t.forward(20)

t.left(270)

t.forward(10)

t.left(315)

t.pendown()

t.forward(60)

t.right(90)

t.left(315)

t.penup()

t.forward(45)

t.right(135)

t.pendown()

t.forward(60)

t.end_fill()

t.penup()

t.home()

t.left(180)

t.forward(150)

t.pendown()

t.left(270)

t.forward(180)

t.left(180)

t.pen(pencolor="black", pensize=5)

t.forward(450)

t.pen(pencolor="blue", pensize=1)

t.penup()

t.home()

t.pendown()
