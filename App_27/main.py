from tkinter import *

def calculate():
    miles = float(miles_entry.get())
    km = miles * 1.609
    km_convert.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_convert = Label(text="0")
km_convert.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()