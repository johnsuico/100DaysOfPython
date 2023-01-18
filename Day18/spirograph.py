from turtle import Turtle, Screen
import random

def spiro(num_circles):
    degrees = 360/num_circles

    for i in range(num_circles):
        t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.circle(80)
        t.right(degrees)

t = Turtle()
screen = Screen()
screen.colormode(255)
t.speed(0)

spiro(60)

screen.exitonclick()