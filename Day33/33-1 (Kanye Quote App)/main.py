from tkinter import *
import os, requests

dirname = os.path.dirname(__file__)
background_path = os.path.join(dirname, './background.png')
kanye_path = os.path.join(dirname, './kanye.png')


def get_quote():
    kanye_quote = requests.get(url = 'https://api.kanye.rest')
    kanye_quote.raise_for_status()
    quote = kanye_quote.json()
    canvas.itemconfig(quote_text, text=quote['quote'])



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=background_path)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 16, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=kanye_path)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()