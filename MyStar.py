import turtle

canvas = turtle.getscreen()

my_turtle = turtle.Turtle()

canvas.title("MyStar")

my_turtle.pu()
my_turtle.goto(0,0)
my_turtle.pd()

my_turtle.color("red")
my_turtle.begin_fill()

for i in range(5):
    my_turtle.forward(100)
    my_turtle.right(144)
   


