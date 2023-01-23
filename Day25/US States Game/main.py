import os, time
from turtle import Screen, Turtle
import pandas as pd

dirname = os.path.dirname(__file__)
state_path = os.path.join(dirname, './50_states.csv')
bg_path = os.path.join(dirname, './blank_states_img.gif')

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic(bg_path)

data = pd.read_csv(state_path)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?").title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.ht()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

