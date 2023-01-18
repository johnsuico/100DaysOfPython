from turtle import Turtle, Screen
import random

def draw_shape(amount_of_sides):
    degrees = 360/amount_of_sides
    turtle.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    for i in range(0, amount_of_sides):
        turtle.forward(100)
        turtle.right(degrees)

turtle = Turtle()
screen = Screen()
screen.colormode(255)

for i in range(4, 9):
    draw_shape(i)

screen.exitonclick()