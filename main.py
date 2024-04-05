import random
import pandas
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}
try:
    csv_data = (pandas.read_csv("data/words_to_learn.csv"))
except FileNotFoundError:
    original_data = (pandas.read_csv("data/french_words.csv"))
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = csv_data.to_dict(orient="records")


def generate_random():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(csv_data['French'][random.randint(0, 100)])
    canvas.itemconfig(card_text, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(card_text, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_random()


window = Tk()
window.title("Flesh Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526,  bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_image)
card_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, 'italic'))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_image, highlightthickness=0, command=generate_random)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)


generate_random()

window.mainloop()
