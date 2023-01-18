from turtle import Turtle, Screen
import random

colors = [
    (96,66,68),     # Brown
    (255,219,185),  # light brown
    (160,57,38),    # Red brownish
    (4,90,151),     # Navy blueish
    (234,169,129),  # Skin toneish
    (246,178,71),   # Mustrad yellowish
    (142,134,51),   # Dark greenish
    (154,168,19),   # Light greenish
    (189,158,8),    # Yellow greenish
    (189,199,174),  # Gray blue
    (195,43,19),    # Redish
    (246,235,207),  # light whiteish
    (133,165,188),  # Mute blue
]

def draw_dots(num_dots, offset):
    for i in range(num_dots):
        t.dot(25, random.choice(colors))
        t.fd(50)
    
    t.home()
    y_pos = t.ycor()
    t.sety(y_pos+offset)

def create_painting(num_rows, num_columns):
    offset = 50
    for i in range(num_rows):
        draw_dots(num_columns, offset)
        offset += 50

t = Turtle()
t.hideturtle()
t.pu()
t.speed('fastest')
screen = Screen()
screen.colormode(255)

create_painting(10, 10)

screen.exitonclick()