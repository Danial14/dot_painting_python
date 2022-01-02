# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
from turtle import Turtle, Screen
myTutle = Turtle()
screen = Screen()
colors = [(187, 162, 20), (154, 80, 34), (25, 85, 139), (24, 59, 125), (227, 127, 98), (27, 9, 5), (235, 213, 86), (4, 189, 143), (222, 154, 211), (70, 1, 2), (214, 56, 47), (174, 4, 3), (176, 3, 6), (227, 160, 214), (31, 48, 81), (139, 162, 185)]
screen.colormode(255)
myTutle.hideturtle()
myTutle.setheading(225)
myTutle.penup()
myTutle.forward(300)
myTutle.pendown()
myTutle.setheading(0)
x_axis = myTutle.pos()[0]
for __ in range(10):
    for _ in range(10):
        myTutle.dot(20, random.choice(colors))
        myTutle.penup()
        myTutle.forward(50)
        myTutle.pendown()
    myTutle.penup()
    position = list(myTutle.pos())
    position[0] = x_axis
    position[1] = position[1] + 50
    position = tuple(position)
    myTutle.setposition(position)
screen.exitonclick()
