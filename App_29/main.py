from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    messagebox.askyesnocancel(title=f"{website}", message="Are you sure you want to proceed?")

    with open("password.txt", "w") as data_file:
        data_file.write(f"{website} | {email} | {password}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("ByteWarden Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(window, width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(window, text="Website:", bg="white")
website_label.grid(column=0, row=1)
email_label = Label(window, text="Email:", bg="white")
email_label.grid(column=0, row=2)
password_label = Label(window, text="Password:", bg="white")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35, bg="white")
website_entry.grid(column=1, columnspan=2, row=1, sticky="w")
email_entry = Entry(width=35, bg="white")
email_entry.grid(column=1, columnspan=2, row=2, sticky="w")
password_entry = Entry(width=21, bg="white")
password_entry.grid(column=1, row=3, sticky="w")

#Buttons
generate_password = Button(text="Generate Password",width=14, bg="white")
generate_password.grid(column=2, row=3, sticky="e")
add_password = Button(text="Add Password", width=36, bg="white", command=save)
add_password.grid(column=1, columnspan=2, row=4, sticky="w")

window.mainloop()


# command=generate_password,
# command=add_password