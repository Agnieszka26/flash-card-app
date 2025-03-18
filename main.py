from tkinter import  *
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Card App Capstone")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)




#------------------------------------- Interface UI  ----------------------------------------------#
ok_img=PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400,263, image=front_card_img)
canvas.create_text(400, 150,font=("Ariel", 40, "italic"), text="French" )
canvas.create_text(400, 263, font=("Ariel", 60, "bold"), text="word")
canvas.grid(column=0, row=0,columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=1, row=1)

ok_button= Button(image=ok_img, highlightthickness=0)
ok_button.grid(column=0, row=1)


window.mainloop()
