import turtle

#*************For loop to write numbers in each sqaure***********#
def numbers():
    for i in range (1,26):
        turtle.color("red2")
        turtle.write(i, "assign = center", font =("arial", 17, "italic", "bold"))
        turtle.forward(-100)
        
        
        if i == 4:
            turtle.goto(200,-220)
        if i == 5:
            turtle.goto(200,-110)
        if i == 6:
            turtle.goto(90,-110)
        if i == 7:
            turtle.goto(-20,-110)
        if i == 8:
            turtle.goto(-130,-110)
        if i == 9:
            turtle.goto(-245,-110)
        if i == 10:
            turtle.goto(-245,0)
        if i == 11:
            turtle.goto(-135,0)
        if i == 12:
            turtle.goto(-25,0)
        if i == 13:
            turtle.goto(90,0)
        if i == 14:
            turtle.goto(195,0)
        if i == 15:
            turtle.goto(195,110)
        if i == 16:
            turtle.goto(90,110)
        if i == 17:
            turtle.goto(-25,110)
        if i == 18:
            turtle.goto(-135,110)
        if i == 19:
            turtle.goto(-245,110)
        if i == 20:
            turtle.goto(-245,220)
        if i == 21:
            turtle.goto(-135,220)
        if i == 22:
            turtle.goto(-25,220)
        if i == 23:
            turtle.goto(90,220)
        if i == 24:
            turtle.goto(195,220)
numbers()
