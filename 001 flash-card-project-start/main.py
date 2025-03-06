import pandas
from tkinter import *
import random as r

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")

try:
    data = pandas.read_csv("./data/words_to_study.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    data_dict = data.to_dict(orient="records")
current_word={}



def next_card():

    global current_word, timer
    current_word = r.choice(data_dict)
    canvas.itemconfig(front_card, image=front_card_img)
    canvas.itemconfig(word_text, text=current_word["French"],fill="black")
    canvas.itemconfig(title_text, text="French",fill="black")
    window.after_cancel(timer)
    timer = window.after(3000, back_card)
def is_known():
    global data_dict,current_word

    data_dict.remove(current_word)
    df = pandas.DataFrame(data_dict)
    df.to_csv("./data/words_to_study.csv",index=False)

    next_card()

def back_card():
    global back_card_img
    canvas.itemconfig(front_card, image=back_card_img)
    canvas.itemconfig(word_text, text=current_word["English"],fill="white")
    canvas.itemconfig(title_text, text="English",fill="white")


timer=window.after(3000, back_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
front_card = canvas.create_image(400, 263, image=front_card_img)
canvas.config(highlightthickness=0)
word_text = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
title_text = canvas.create_text(400, 63, text="Title", font=("Arial", 40, "normal"))
canvas.grid(row=0, column=0, columnspan=2)
check_img = PhotoImage(file="./images/right.png")
cross_img = PhotoImage(file="./images/wrong.png")
right_button = Button(image=check_img, highlightthickness=0, command=is_known)
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()
