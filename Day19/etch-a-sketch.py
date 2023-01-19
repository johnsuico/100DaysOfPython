from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def move_forwards():
    t.forward(20)

def move_backwards():
    t.backward(20)

def rotate_right():
    t.right(10)

def rotate_left():
    t.left(10)

def reset():
    t.reset()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(rotate_right, "d")
screen.onkey(rotate_left, "a")
screen.onkey(reset, "c")
screen.exitonclick()