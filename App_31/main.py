from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)

def next_card():
    current_card = random.choice(to_learn)
    print(current_card["French"])

#GUI
window = Tk()
window.title("Flashed")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Minecraft", 40, "italic", "underline"))
canvas.create_text(400, 263, text="word", font=("Minecraft", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
unknown = Button(image=wrong_img, highlightthickness=0, command=next_card)
unknown.grid(row=1, column=0)

correct_img = PhotoImage(file="images/right.png")
known = Button(image=correct_img, highlightthickness=0, command=next_card)
known.grid(row=1, column=1)




window.mainloop()