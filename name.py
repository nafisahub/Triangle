import turtle

def triangle(side_length, colour):
    angle = 120
    turtle.color(colour, colour)
    turtle.begin_fill()
    for side in range(4):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.end_fill()

triangle(300, 'red')
triangle(220, 'pink')
triangle(150, 'blue')
triangle(80, 'yellow')
