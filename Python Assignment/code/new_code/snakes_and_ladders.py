import turtle
import random


#*************Setup Parameters***********#
def main():
    
    turtle.title("Snakes and ladders game")
    turtle.setup(900,800,0,0)
    turtle.penup()
    turtle.goto(-250,250)
    turtle.width(3)
    turtle.speed(100000)
    turtle.pendown()
    turtle.bgcolor("ivory")
    turtle.hideturtle()
    turtle.color("navy")
    
#*************Draws layout of Board***********#
    for i in range(4):
        turtle.forward(550)
        turtle.right(90)
main()

from squares import squares

from numbers import numbers

from gameinterface import ladders, snake, players, stretch, gamesetup











