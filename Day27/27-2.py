from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# Label placed at grid (1,1)
my_label = Label(text='I am a label', font=('arial', 16, 'bold'))
my_label.grid(row=0, column=0)

# Button at (2, 2)
def button_clicked():
    my_label.config(text='Button one clicked')

button_one = Button(text='Click me', command=button_clicked)
button_one.grid(row=1, column=1)

# Another button at (0, 2)
button_two = Button(text='Button2')
button_two.grid(row=0, column=2)

# Entry box at (3, 2)
input = Entry(width=10)
input.grid(row=3, column=3)

window.mainloop()