BACKGROUND_COLOR = "#B1DDC6"

import tkinter, os, random, pandas as pd

# Font vars
LANGUAGE_FONT = ('Arial', 40, 'italic')
WORD_FONT = ('Arial', 60, 'bold')
CURRENT_WORD = {}

# Flip Card
def flip_card():
    global CURRENT_WORD
    canvas.itemconfig(flash_img, image=card_back_image)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=CURRENT_WORD['English'], fill='white')

# Get random word and display on card
def next_card():
    global CURRENT_WORD, FLIP_TIMER
    window.after_cancel(FLIP_TIMER)
    CURRENT_WORD = random.choice(french_data_dict)
    canvas.itemconfig(flash_img, image=card_front_image)
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=CURRENT_WORD['French'], fill='black')

    # Flip card to english after 3 sec
    FLIP_TIMER = window.after(3000, func=flip_card)

# User knows the word
def is_known():
    french_data_dict.remove(CURRENT_WORD)
    data = pd.DataFrame(french_data_dict)
    data.to_csv(words_to_learn_path, index=False)
    next_card()

# Image paths
card_back_path = os.path.join(os.path.dirname(__file__), './images/card_back.png')
card_front_path = os.path.join(os.path.dirname(__file__), './images/card_front.png')
right_path = os.path.join(os.path.dirname(__file__), './images/right.png')
wrong_path = os.path.join(os.path.dirname(__file__), './images/wrong.png')

# Data paths and getting data
french_words_path = os.path.join(os.path.dirname(__file__), './data/french_words.csv')
words_to_learn_path = os.path.join(os.path.dirname(__file__), './data/word_to_learn.csv')

try:
    french_data = pd.read_csv(words_to_learn_path)
except FileNotFoundError:
    french_data = pd.read_csv(french_words_path)

french_data_dict = french_data.to_dict(orient='records')

# Setting up tkinter
window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Creating canvas for flash image
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = tkinter.PhotoImage(file=card_back_path)
card_front_image = tkinter.PhotoImage(file=card_front_path)
flash_img = canvas.create_image(400, 263, image=card_front_image)
language_text = canvas.create_text(400, 150, text='', fill='black', font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 263, text='', fill='black', font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_btn_img = tkinter.PhotoImage(file=wrong_path)
right_btn_img = tkinter.PhotoImage(file=right_path)

wrong_button = tkinter.Button(image=wrong_btn_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button = tkinter.Button(image=right_btn_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

# Flip card
FLIP_TIMER = window.after(3000, func=flip_card)

# Get random word to display
next_card()

window.mainloop()