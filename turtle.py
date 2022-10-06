import turtle
# turtle.init()

def star():
    for step in range(6):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.right(360 / 3)
        turtle.end_fill()

        turtle.forward(50)
        turtle.right(60)
    turtle.done()


turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('blue')
turtle.speed(10)


star()
