import turtle
import random


# *********** setup ladders on board**********#

def ladders():
    turtle.goto(0, 0)
    turtle.speed(1)

    l = turtle.Turtle()
    l.penup()
    l.goto(-80, -80)
    turtle.addshape("ladder.gif")
    l.shape("ladder.gif")

    l2 = turtle.Turtle()
    l2.penup()
    turtle.addshape("ladder2.gif")
    l2.shape("ladder2.gif")
    l2.goto(30, 140)

    l3 = turtle.Turtle()
    l3.penup()
    turtle.addshape("ladder3.gif")
    l3.shape("ladder3.gif")
    l3.goto(250, -135)


ladders()


# ***********Function to setup snakes on board************#

def snake():
    s = turtle.Turtle()
    s.penup()
    turtle.addshape("snake.gif")
    s.shape("snake.gif")
    s.goto(150, 90)

    s2 = turtle.Turtle()
    s2.penup()
    turtle.addshape("snake2.gif")
    s2.shape("snake2.gif")
    s2.goto(40, -190)

    s3 = turtle.Turtle()
    turtle.addshape("snake3.gif")
    s3.penup()
    s3.shape("snake3.gif")
    s3.goto(-180, -70)


snake()

# **************Adds player's gifs***************#

bull = turtle.Turtle()
cow = turtle.Turtle()


def players():
    bull.penup()
    turtle.addshape("bull.gif")
    bull.shape("bull.gif")
    bull.goto(-210, -270)
    turtle.hideturtle()

    cow.penup()
    turtle.addshape("cow.gif")
    cow.shape("cow.gif")
    cow.goto(-210, -225)


players()

# ********** User interface of the game**************#
print("New Game!")
print("Type yes to turn on dark mode or press enter to skip")
dark_mode = input()
if dark_mode == "yes":
    turtle.bgcolor("dimgray")

player1_name = input("Type your name to choose bull ")
if player1_name == '':
    player1_name = 'Big Bad Bull'
print('Welcome: {}'.format(player1_name))
player2_name = input("Type your name to choose cow ")
if player2_name == '':
    player2_name = 'Fluffy Cow'
print('Welcome: {}'.format(player1_name))

ply = turtle.Turtle()
ply.penup()
ply.hideturtle()
style = ("arial", 17, "italic", "bold")
ply.goto(-70, 280)
ply.write(player1_name, "assign = center", font=style)

ply.goto(20, 280)
ply.write("vs", "assign = center", font=style)

ply.goto(65, 280)
ply.write(player2_name, "assign = center", font=style)

square = 1  # **Keeps track of the square**#
square_2 = 1
dice_roll = random.randint(1, 6)  # **To display random numbers for the dice**#
dice = turtle.Turtle()
win = turtle.Turtle()
win.hideturtle()


# ***setup dice and players movement***#

def gamesetup():
    dice.penup()
    dice.hideturtle()
    dice.setpos(-350, -20)
    turtle.addshape("dice1.gif")
    turtle.addshape("dice2.gif")
    turtle.addshape("dice3.gif")
    turtle.addshape("dice4.gif")
    turtle.addshape("dice5.gif")
    turtle.addshape("dice6.gif")

    # ***********While loop for the players turn and dice roll**************#
    while True:

        dice_roll = random.randint(1, 6)
        print(player1_name, "press enter to roll the dice")
        a = input()
        print(player1_name, "rolled", dice_roll)
        dice.showturtle()

        if dice_roll == 1:
            dice.shape("dice1.gif")
        elif dice_roll == 2:
            dice.shape("dice2.gif")
        elif dice_roll == 3:
            dice.shape("dice3.gif")
        elif dice_roll == 4:
            dice.shape("dice4.gif")
        elif dice_roll == 5:
            dice.shape("dice5.gif")
        elif dice_roll == 6:
            dice.shape("dice6.gif")

        global square
        global square_2
        for i in range(1, (dice_roll + 1)):
            square = square + 1
            bull.forward(107)

            curr_pos = bull.pos()

            if curr_pos[0] + 107 > 230:
                bull.left(90)

            if curr_pos[0] + 107 < -100:
                bull.right(90)

            if square == 22 and dice_roll >= 4:
                bull.backward(110)
                sqaure = 21
            if square == 23 and dice_roll >= 3:
                bull.backward(210)
                square = 21
            if square == 24 and dice_roll >= 2:
                bull.backward(310)
                square = 21

            if square >= 25:
                turtle.addshape("win.gif")
                win.shape("win.gif")
                win.showturtle()

                input("Press enter to start new game")
                bull.reset()
                cow.reset()
                bull.penup()
                cow.penup()
                win.hideturtle()
                bull.goto(-210, -270)
                cow.goto(-210, -225)
                square = 1
                square_2 = 1

        if square == 5:
            bull.forward(220)
            square = 15

        elif square == 8:
            bull.goto(-10, -270)
            square = 3
            bull.right(180)

        elif square == 9:
            bull.goto(-110, -50)
            square = 12
            bull.right(180)

        elif square == 18:
            bull.goto(0, 170)
            square = 23
            bull.right(180)

        elif square == 20:
            bull.goto(-210, -270)
            square = 1
            bull.right(90)

        elif square == 24:
            bull.goto(100, -50)
            square = 14

        elif square >= 25:
            bull.goto(210, 170)
            break

        print("Big Bad Bull is at square ", square)

        print(player2_name, "Press enter to roll the dice")
        b = input()
        dice_roll = random.randint(1, 6)
        print(player2_name, "rolled", dice_roll)

        if dice_roll == 1:
            dice.shape("dice1.gif")
        elif dice_roll == 2:
            dice.shape("dice2.gif")
        elif dice_roll == 3:
            dice.shape("dice3.gif")
        elif dice_roll == 4:
            dice.shape("dice4.gif")
        elif dice_roll == 5:
            dice.shape("dice5.gif")
        elif dice_roll == 6:
            dice.shape("dice6.gif")

        for i in range(1, (dice_roll + 1)):
            square_2 = square_2 + 1
            cow.forward(107)

            current_pos = cow.pos()
            if (current_pos[0] + 107 > 230):
                cow.left(90)

            if (current_pos[0] + 107 < -100):
                cow.right(90)

            if square_2 >= 25:
                turtle.addshape("win.gif")
                win.shape("win.gif")
                win.showturtle()

                input("press Enter to start new game")
                print("New game!")
                cow.reset()
                bull.reset()
                cow.penup()
                bull.penup()
                win.hideturtle()
                cow.goto(-210, -270)
                bull.goto(-210, -270)
                square_2 = 1
                square = 1

        if square_2 == 5:
            cow.forward(220)
            square_2 = 15

        elif square_2 == 8:
            cow.goto(-10, -225)
            cow.right(180)
            square_2 = 3

        elif square_2 == 9:
            cow.right(90)
            cow.forward(120)
            cow.right(90)
            square_2 = 12

        elif square_2 == 18:
            cow.right(90)
            cow.forward(120)
            cow.right(90)
            square_2 = 23

        elif square_2 == 20:
            cow.goto(-210, -225)
            cow.right(90)
            square_2 = 1

        elif square_2 == 24:
            cow.goto(100, -30)
            square_2 = 14

        elif square_2 >= 25:
            cow.goto(210, 125)
            break

        print("Fluffy cow is at Square ", square_2)


gamesetup()
