import turtle
canvas= turtle.getscreen()
my_turtle= turtle.Turtle()

canvas.title("My Name")

#Draw a rectangle
my_turtle.pu()
my_turtle.goto(-150,-50)
my_turtle.pd()

my_turtle.fillcolor("blue")
my_turtle.begin_fill()

for i in range(4):
    if i % 2 == 0:
        my_turtle.forward(300)
        my_turtle.left(90)
    else:
        my_turtle.forward(100)
        my_turtle.left(90)
my_turtle.end_fill()

my_turtle.pu()
my_turtle.goto(-50,0)
my_turtle.pd()
my_turtle.color("red")
#my_turtle.pensize(1)
my_turtle.write("LeenaAmbekar",font=('Arial',25,'normal'))

#turtle.done()
