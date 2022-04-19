import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data = []

try:
    data = pandas.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv").to_dict(orient="records")
except pandas.errors.EmptyDataError:
    pass


def generate_random_card():
    global current_card, flip_timer
    if data:
        window.after_cancel(flip_timer)
        current_card = random.choice(data)
        canvas.itemconfig(card_background, image=CARD_FRONT_IMG)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, func=flip_card)
    else:
        current_card = {}
        canvas.itemconfig(card_title, text="Congratulation", fill="black")
        canvas.itemconfig(card_word, text="you learn every word.", fill="black")


def right_answer():
    if current_card:
        data.remove(current_card)
        pandas.DataFrame(data).to_csv("data/words_to_learn.csv", index=False)
    generate_random_card()


def flip_card():
    if current_card:
        canvas.itemconfig(card_background, image=CARD_BACK_IMG)
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

CARD_BACK_IMG = PhotoImage(file="images/card_back.png")
CARD_FRONT_IMG = PhotoImage(file="images/card_front.png")
WRONG_BUTTON_IMG = PhotoImage(file="images/wrong.png")
RIGHT_BUTTON_IMG = PhotoImage(file="images/right.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=CARD_FRONT_IMG)
card_title = canvas.create_text(400, 150, fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=WRONG_BUTTON_IMG, highlightthickness=0, bd=0, command=generate_random_card)
wrong_button.grid(column=0, row=1)
right_button = Button(image=RIGHT_BUTTON_IMG, highlightthickness=0, bd=0, command=right_answer)
right_button.grid(column=1, row=1)

generate_random_card()
window.mainloop()
