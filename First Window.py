from ezgraphics import GraphicsWindow

win = GraphicsWindow()
#win2 = GraphicsWindow(200,100)

win.setTitle("My First Drawing")
canvas = win.canvas()

canvas.drawRectangle(40, 40, 100, 200)
canvas.drawRectangle(200, 200, 150, 50)

win.wait()
