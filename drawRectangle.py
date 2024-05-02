from ezgraphics import GraphicsWindow

win = GraphicsWindow()

canvas = win.canvas()
canvas.setOutline("green")
canvas.setFill(64, 255, 64) #"red"
#canvas.fill("blue")
canvas.drawRect(0,0,50,100)

canvas.drawOval(200,100,200,200)

canvas.drawText(10,10,"Hello")

canvas.drawLine(400,200,0,0)
win.wait
