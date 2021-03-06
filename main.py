from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_flag, image=flag_image_fr)
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    """Remove the current card from the to_learn-dictionary and put it in the cards_learned dictionary. """
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_flag, image=flag_image_gb)
    canvas.itemconfig(card_background, image=card_back_img)


# ---------------------------------- Load data -------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------------- Generate UI -------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
flag_image_fr = PhotoImage(file="images/fr-flag.png").subsample(4, 4)
flag_image_gb = PhotoImage(file="images/gb-flag.png").subsample(4, 4)

canvas = Canvas()
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(width=800, height=526)
canvas.config(highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_flag = canvas.create_image(50, 50, image=flag_image_fr, )
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=is_known)
unknown_button.grid(row=1, column=0)

next_card()

window.mainloop()
