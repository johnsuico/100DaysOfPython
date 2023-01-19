from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)
screen.setup(500, 400)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [-70, -40, -10, 20, 50, 80]
turtles = []

user_bet = screen.textinput(title= "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")

for i in range(0, 6):
    t = Turtle(shape="turtle")
    t.pu()
    t.color(colors[i])
    t.goto(x = -230, y = y_pos[i])
    turtles.append(t)

if user_bet:
    race = True

while race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"Your turtle, {user_bet}, won the race.")
            else:
                print(f"Your turtle, {user_bet}, did not win the race.")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()