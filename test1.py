from ezgraphics import GraphicsImage, GraphicsWindow

filename = "queen-mary.gif"
image = GraphicsImage(filename)
#We draw the image on the canvas of a GraphicsWindow
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()
