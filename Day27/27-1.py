from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)

# Label
my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack()

def button_clicked():
    my_label.config(text='Button got clicked')

# Button
button = Button(text='Click me', command=button_clicked)
button.pack()

def submit():
    user_input = input.get()
    my_label.config(text=user_input)

# Entry
input = Entry(width=10)
input.pack()
button = Button(text='Submit', command=submit)
button.pack()

window.mainloop()