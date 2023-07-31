from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


button_wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0)
button_wrong.grid(row=1, column=0)

button_right_img = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0)
button_right.grid(row=1, column=1)

window.mainloop()
