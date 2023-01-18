from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
screen.colormode(255)

directions = [0, 90, 180, 270]

t.pensize(10)
t.speed(0)
for i in range(200):
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.forward(25)
    t.setheading(random.choice(directions))


screen.exitonclick()