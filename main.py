from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------------- Load data -------------------------- #

language_data = pandas.read_csv("data/french_words.csv")
print(language_data)

# ---------------------------------- Generate UI -------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)

window.config(padx=50, pady=50)
card_image = PhotoImage(file="images/card_front.png")
fr_flag = PhotoImage(file="images/fr-flag.png").subsample(4, 4)
card_canvas = Canvas()
card_canvas.create_image(400, 263, image=card_image)
card_canvas.config(width=800, height=526)
card_canvas.config(highlightthickness=0)
card_canvas.config(bg=BACKGROUND_COLOR)
card_canvas.grid(row=0, column=0, columnspan=2)

card_canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_canvas.create_image(50, 50, image=fr_flag, )
card_canvas.create_text(400, 263, text="Baguette", font=("Arial", 60, "bold"))

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

window.mainloop()
