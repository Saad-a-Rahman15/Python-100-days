from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        with open("password.json", "w") as data_file:
            json.dump(new_data, data_file)
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


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
generate_password = Button(text="Generate Password",width=14, bg="white", command=password_generator)
generate_password.grid(column=2, row=3, sticky="w")
add_password = Button(text="Add Password", width=36, bg="white", command=save)
add_password.grid(column=1, columnspan=2, row=4, sticky="w")

window.mainloop()


# command=generate_password,
# command=add_password