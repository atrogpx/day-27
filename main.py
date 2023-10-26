from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    number_label.config(text=km)

window = Tk()
window.title("My First GUI Window")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

number_label = Label(text="0")
number_label.grid(column=1, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

input = Entry(width=7)
input.grid(column=1, row=0)

window.mainloop()