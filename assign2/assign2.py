import turtle
import math
import random

# ------------------------------- SETUP WINDOW
window = turtle.Screen()
window.bgcolor('blue')

# ------------------------------- SETUP TURTLES
tree = turtle.Turtle()
tree.hideturtle()
tree.penup()
tree.speed(0)

snowMan = turtle.Turtle()
snowMan.hideturtle()
snowMan.penup()
snowMan.speed(0)

# ------------------------------- DRAWING TREES
treeOldY = (200)       # this will be used to store the Y coordinate of the tree
for i in range(7):     # range is equal to how many trees will be drawn
    tree.goto(random.randint(-300, 300), random.randint(0, 150))    # send turtle to random coordinates

# Note: This block of code makes sure a smaller tree is not stacked on top of a larger tree
    treeNewY = (tree.position()[1])
    if treeNewY > treeOldY:
        treeNewY = treeOldY - 10

# Note: if the turtle position needed to be changed. This block of code will movie it
# This block of code also stores the starting coordinates so we can send later send the-›
# turtle back to the starting point
    tree.goto(tree.position()[0], treeNewY)
    treeStart = (tree.position()[0], tree.position()[1])

# Note: this makes sure that trees with a higher y coordinate are drawn smaller
# Thus making the scene more realistic
    if tree.position()[1] > 150:
        randLength = random.randint(2, 4)
    elif tree.position()[1] > 50:
        randLength = random.randint(4, 6)
    else:
        randLength = random.randint(6, 8)

# ------------- Tree trunk
    tree.pendown()
    tree.fillcolor('#7D3701')
    tree.begin_fill()
    tree.forward(8 * randLength)
    tree.left(90)
    tree.forward(5 * randLength)
    tree.left(90)
    tree.forward(8 * randLength)
    tree.left(90)
    tree.forward(5 * randLength)
    tree.end_fill()

# Note: This section resets the turtle position and stores two sets of coordinates to be used later
    tree.backward(5 * randLength)
    tree.left(90)
    tree.forward(4 * randLength)
    treeMidpoint = (tree.position()[0])     # x coordinate for center of tree
    tree.backward(4 * randLength)
    bottomTriangle = (tree.position()[0], tree.position()[1])   # Starting point at bottom of triangle

# ------------- Tree leafs
    for i in range(3):
        tree.pendown()
        tree.fillcolor('green')
        tree.begin_fill()
        tree.forward(8 * randLength)
        tree.forward(5 * randLength)
        tree.left(120)
        tree.forward(4 * randLength)
        tree.left(60)
        tree.goto(bottomTriangle[0], tree.position()[1])
        tree.penup()
        tree.goto(bottomTriangle)
        tree.pendown()
        tree.forward(5 * randLength)
        tree.right(120)
        tree.forward(4 * randLength)
        tree.goto(bottomTriangle[0], tree.position()[1])
        tree.end_fill()
        tree.penup()
        tree.right(60)
        bottomTriangle = (tree.position()[0], tree.position()[1])   # resets bottom triage for next loop

# ------------- Tree top
    tree.goto(bottomTriangle)
    tree.pendown()
    tree.begin_fill()
    tree.forward(8 * randLength)
    tree.forward(5 * randLength)
    tree.left(120)
    tree.goto(treeMidpoint, tree.position()[1] + (8 * randLength))
    tree.left(60)
    tree.penup()
    tree.goto(bottomTriangle)
    tree.pendown()
    tree.forward(5 * randLength)
    tree.right(120)
    tree.goto(treeMidpoint, tree.position()[1] + (8 * randLength))
    tree.end_fill()
    tree.penup()
    tree.right(60)          # reset turtle to original heading
    tree.goto(treeStart)    # resend turtle to starting point
    treeOldY = (tree.position()[1])

# ------------------------------- DRAWING SNOWMAN

# ------------ MATH FOR DRAWING CIRCLE & VARIABLES
# Note: Everything pertaining to the drawing of the snowman is based off of 'radius'
# changing this value will also change the size of everything else regaurding the snowman (hat, eyes, body size, etc.)
radius = 110
# Note: increasing 'speedFactor' will increase the speed at which the snosman is drawn
# but will also slightly skew the length traveled for every roation and trhow off the value
# 'radius' so keep this number low. 
speedFactor = 8
shrinkFactor = 1.2  # controls how much snowman shrinks in the positive vertical direction
radius2 = radius / shrinkFactor  # radius of middle circle of snowman
radius3 = radius / (shrinkFactor ** 2)  # radius of snowman head
diamater = radius * 2
diamater2 = radius2 * 2
diamater3 = radius3 * 2
lengthPerDeg = (((2 * math.pi * radius) / 360) * speedFactor)   # length turtle travels for every turn

# ------------- Bottom of snowman
snowMan.goto(0 - (lengthPerDeg / 2), -300)
# Note: 'bottomCirclePosition' is simply a refrance point to send the turtle back to
# in order to add accessores such as eyes.
bottomCirclePosition = (snowMan.position()[0], snowMan.position()[1]) 
snowMan.pendown()
snowMan.fillcolor('white')
snowMan.begin_fill()
for i in range(int(360 / speedFactor)):
    snowMan.forward(lengthPerDeg)
    snowMan.left(speedFactor)
snowMan.penup()
snowMan.end_fill()

# ------------- Middle of snowman
snowMan.goto(snowMan.position()[0], snowMan.position()[1] + diamater)
# Note: 'middleCirclePosition' is simply a refrance point to send the turtle back to
# in order to add accessores such as eyes.
middleCirclePosition = (snowMan.position()[0], snowMan.position()[1])
snowMan.pendown()
snowMan.fillcolor('white')
snowMan.begin_fill()
for i in range(int(360 / speedFactor)):
    snowMan.forward(lengthPerDeg / shrinkFactor)
    snowMan.left(speedFactor)
snowMan.penup()
snowMan.end_fill()

# ------------- Top of snowman
snowMan.goto(snowMan.position()[0], snowMan.position()[1] + diamater2)
# Note: 'topCirclePosition' is simply a refrance point to send the turtle back to
# in order to add accessores such as eyes.
topCirclePosition = (snowMan.position()[0], snowMan.position()[1])
snowMan.pendown()
snowMan.fillcolor('white')
snowMan.begin_fill()
for i in range(int(360 / speedFactor)):
    snowMan.forward(lengthPerDeg / (shrinkFactor ** 2))
    snowMan.left(speedFactor)
snowMan.penup()
snowMan.end_fill()

# ------------- Snowman eyes
# Positioning turtle
snowMan.goto(snowMan.position()[0], snowMan.pos()[1] + ((diamater3 / 4) * 2.5))
snowMan.forward(lengthPerDeg / (shrinkFactor ** 2) / 2)

snowMan.forward(diamater3 / 4)
snowMan.dot(radius / 7, 'black')
snowMan.right(180)
snowMan.forward((diamater3 / 4) * 2)
snowMan.dot(radius / 7, 'black')

# ------------- Snowman nose
#positioning turtle
snowMan.right(180)
snowMan.forward(diamater3 / 4)
snowMan.right(90)

snowMan.forward(radius3 / 5)
snowMan.dot(radius / 6, 'orange')
snowMan.forward(radius3 / 8)
snowMan.dot(radius / 7, 'orange')
snowMan.forward(radius / 10)
snowMan.dot(radius / 8, 'orange')
snowMan.penup()

# ------------- Snowman top hat
# Positioning turtle
snowMan.goto(topCirclePosition)
snowMan.left(90)
snowMan.forward(lengthPerDeg / (shrinkFactor ** 2) / 2)
snowMan.left(90)
snowMan.forward(diamater3 - (diamater3 / 10))

snowMan.right(90)
snowMan._pensize = 4
snowMan.pendown()
snowMan.fillcolor('darkgray')
snowMan.begin_fill()
snowMan.forward(radius3 / 1.2)  # east
snowMan.left(90)
snowMan.forward(radius3 / 4)    # north
snowMan.left(90)
snowMan.forward(radius3 / 2.8)  # west
snowMan.right(90)
snowMan.forward(radius3 / 1.6)  # north
snowMan.left(90)
snowMan.forward(radius3)  # west
snowMan.left(90)
snowMan.forward(radius3 / 1.6)  # south
snowMan.right(90)
snowMan.forward(radius3 / 2.9)  # west
snowMan.left(90)
snowMan.forward(radius3 / 4)    # shouth
snowMan.left(90)
snowMan.forward(radius3 / 1.2)  # east
snowMan.end_fill()
snowMan.penup()

# ------------- Snowman buttons
#positioning turtle
snowMan.goto(topCirclePosition)
snowMan.forward(lengthPerDeg / (shrinkFactor ** 2) / 2)
snowMan.right(90)

snowMan.forward(diamater2 / 8.5)
for i5 in range(4):         # Increse or decrease range for more or less buttons
    snowMan.dot(radius / 8, 'red')
    snowMan.forward(diamater2 / 6)

# ------------- Snowman arms and hands
# Positioning turtle
snowMan.goto(middleCirclePosition)
snowMan.left(90)
snowMan.forward((lengthPerDeg / shrinkFactor) / 2)
snowMan.left(90)
snowMan.forward(radius2)
snowMan.right(90)
snowMan.forward(radius2)

# Right arm and hand
snowMan.pendown()
snowMan.forward(radius2 / 1.5)
snowMan.forward(radius2 / 4)
snowMan.backward(radius2 / 4)
snowMan.right(30)
snowMan.forward(radius2 / 4)
snowMan.backward(radius2 / 4)
snowMan.left(60)
snowMan.forward(radius2 / 4)
snowMan.backward(radius2 / 4)
snowMan.penup()

# Send turtle to other side of snowman body
snowMan.right(210)
snowMan.forward(diamater2)
snowMan.forward(radius2 / 1.5)

# Left arm and hand
snowMan.pendown()
snowMan.forward(radius2 / 1.5)
snowMan.forward(radius2 / 4)
snowMan.backward(radius2 / 4)
snowMan.right(30)
snowMan.forward(radius2 / 4)
snowMan.backward(radius2 / 4)
snowMan.left(60)
snowMan.forward(radius2 / 4)
snowMan.backward(radius2 / 4)

window.exitonclick()
