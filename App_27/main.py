from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(500, 300)

label = Label(text="Hi!", font=("Minecraft", 100))
label.pack(expand=True)

def button_clicked():
    label.config(text="Ouch! STOP CLICKING!", fg="red")

def button_clicked_2():
    label.config(text="Thank you!", fg="green")

def button_clicked_3():
    label.config(text="Hi!", fg="black")

button = Button(text="Attack the Button!", font=("Minecraft", 20), command=button_clicked)
button.pack(expand=True)

save = Button(text="Save the Button!", font=("Minecraft", 20), command=button_clicked_2)
save.pack(expand=True)

reset = Button(text="Reset", font=("Minecraft", 20), command=button_clicked_3)
reset.pack(expand=True)


window.mainloop()