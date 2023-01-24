from tkinter import *

FONT = ('Arial', 12, 'normal')

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)

# Initalize result var
result = 0

# Function to convert mile to km
def convert_mile_km():
    mile_input = mile_entry.get()
    result = float(mile_input) * 1.609
    result_label.config(text=result)

# Entry box
mile_entry = Entry(width=10)
mile_entry.grid(column=1, row=0)

# Mile label
mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)
mile_label.config(padx=5)

# Descriptive label
desc_label = Label(text='is equal to', font=FONT)
desc_label.grid(column=0, row=1)

# Converted miles to km label
result_label = Label(text=result, font=FONT)
result_label.grid(column=1, row=1)

# KM sign
km_sign = Label(text='Km', font=FONT)
km_sign.grid(column=2, row=1)
km_sign.config(padx=5)

# Calculate button
calc_button = Button(text='Calculate', command=convert_mile_km)
calc_button.grid(column=1, row=2)

window.mainloop()