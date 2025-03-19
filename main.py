import random
from tkinter import  *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
CSV_FILE = "./data/words_to_learn.csv"
window = Tk()
window.title("Flash Card App Capstone")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

#------------------------------------- READ DATA  -------------------------------#
title = ""
word = ""
flip_timer = None
french_words_dict = {}

try:
    data  = pandas.read_csv(CSV_FILE)
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    french_words_dict = original_data.to_dict(orient="records")
else:
    words_to_learn_dict = data.to_dict(orient="records")

random_record = random.choice(french_words_dict)



def change_card():
    global title, random_record
    title=f"English"
    new_word=random_record[title]
    canvas.itemconfigure(title_label, text=title, fill="white")
    canvas.itemconfigure(word_label, text=new_word, fill="white")
    canvas.itemconfigure(card_background, image=back_card_img)


def read_new_word():
    global word, random_record, title, flip_timer
    title = f"French"
    random_record = random.choice(french_words_dict)
    word=random_record[title]
    canvas.itemconfigure(title_label, text=title, fill="black")
    canvas.itemconfigure(word_label, text=word, fill="black")
    canvas.itemconfigure(card_background, image=front_card_img)
    if flip_timer:
        window.after_cancel(flip_timer)
    flip_timer = window.after(3000, change_card)

#------------------------------------- SAVE PROGRESS ----------------------------#

def remove_known_word():
    global french_words_dict
    french_words_dict.remove(random_record)
    d = pandas.DataFrame(french_words_dict)
    d.to_csv(CSV_FILE, index=False)
    read_new_word()


#------------------------------------- Interface UI  ----------------------------------------------#
ok_img=PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background=canvas.create_image(400,263, image=front_card_img)
title_label = canvas.create_text(400, 150,font=("Ariel", 40, "italic"), text=title )
word_label=canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text=word)
canvas.grid(column=0, row=0,columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=read_new_word)
wrong_button.grid(column=1, row=1)

ok_button= Button(image=ok_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_known_word)
ok_button.grid(column=0, row=1)

read_new_word()

window.mainloop()
