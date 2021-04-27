import turtle

#************For loop to make sqaures inside the board*********#
def squares():
    for i in range(1):
        
        turtle.forward(110)
        turtle.right(90)
        turtle.forward(550)
        turtle.left(90)

        turtle.forward(110)
        turtle.left(90)
        turtle.forward(550)
        turtle.right(90)

        turtle.forward(110)
        turtle.right(90)
        turtle.forward(550)
        turtle.left(90)

        turtle.forward(110)
        turtle.left(90)
        turtle.forward(550)
        turtle.right(90)

        turtle.forward(110)
        turtle.right(90)
        turtle.forward(110)
        turtle.left(90)
        turtle.backward(550)

        turtle.right(90)
        turtle.forward(110)
        turtle.left(90)
        turtle.forward(550)

        turtle.right(90)
        turtle.forward(110)
        turtle.right(90)
        turtle.forward(550)

        turtle.left(90)
        turtle.forward(110)
        turtle.left(90)
        turtle.forward(550)

        turtle.right(90)
        turtle.forward(110)
        turtle.right(90)
        turtle.forward(550)

        turtle.penup()
        turtle.goto(-240,-220)
squares()
