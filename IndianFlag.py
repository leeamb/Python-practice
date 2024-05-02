import turtle

canvas = turtle.getscreen()

t = turtle.Turtle()

canvas.title("Indian Flag")

length = 400 #int(input("PLease enter the length: "))
width = 80 #int(input("PLease enter the width: "))


t.penup()
t.goto(-150,150)
t.pendown()

# draw first rectangle
t.color("orange")
t.begin_fill()
for _ in range(4):
    if _%2 == 0:
        t.forward(length)
        t.left(90)

    else:
        t.forward(width)
        t.left(90)
t.end_fill()
t.color("white")
t.right(90)
t.forward(width)
t.left(90)

# draw Green rectangale
t.color("green")
t.begin_fill()
for _ in range(4):
        if _%2 == 0:
            t.forward(length)
            t.right(90)

        else:
            t.forward(width)
            t.right(90)
t.end_fill()  
    
#blue circle
t.penup()
t.goto(50,73)
t.pendown()
t.color("navy")
t.circle(40)
t.penup()
t.goto(50,113)
t.pendown()
for i in range(24):
    t.forward(40)
    t.backward(40)
    t.left(15)


