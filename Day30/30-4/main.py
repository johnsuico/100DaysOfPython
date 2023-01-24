from tkinter import *
from tkinter import messagebox
import os, random, json

FONT = ('Arial', 16, 'normal')

dirname = os.path.dirname(__file__)
image_path = os.path.join(dirname, './logo.png')
pass_data = os.path.join(dirname, './data.json')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
    [password_list.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]
    [password_list.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showwarning(title='Fields are empty', message='You have left some or all fields empty.')
    else:
        confirm = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email} \nPassword:{password} \nIs this okay to save?')

        if confirm:
            try:
                with open(pass_data, 'r') as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = new_data
            finally:
                with open(pass_data, 'w') as data_file:
                    json.dump(data, data_file, indent=4)
                website_input.delete(0, END)
                password_input.delete(0, END)    

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_input.get()

    if website == "":
        messagebox.showwarning(title='Field is empty', message='Website field is empty. Cannot search.')
    else:
        try:
            with open(pass_data, 'r') as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            messagebox.showerror(title='File not found', message='The current password storage file is empty.')
        else:
            if website in data:
                messagebox.showinfo(title=f'Info for {website}', message=f"Email: {data[website]['email']} \nPassword: {data[website]['password']}")
            else:
                messagebox.showerror(title='Website not found', message='Website not found')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:', font=FONT)
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:', font=FONT)
email_label.grid(column=0, row=2)

password_label = Label(text='Password:', font=FONT)
password_label.grid(column=0, row=3)

# Entry fields
website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, 'test@gmail.com')

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

# Buttons
gen_pass_btn = Button(text='Generate Password', highlightthickness=0, command=generate_pass)
gen_pass_btn.grid(column=2, row=3)

search_btn = Button(text='Search', highlightthickness=0, width=14, command=search)
search_btn.grid(column=2, row=1)

add_btn = Button(text='Add', width=43, highlightthickness=0, command=save_pass)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()