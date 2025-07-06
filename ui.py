from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

class FlashcardUI:
    def __init__(self, window, card_front_img, card_back_img, on_flip, on_mark_known, on_next_card):
        self.canvas = Canvas(window, width=800, height=526)
        self.card_front_img = card_front_img
        self.card_back_img = card_back_img
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        cross_img = PhotoImage(file="images/wrong.png")
        unknown_button = Button(image=cross_img, highlightthickness=0, command=on_next_card)
        unknown_button.image = cross_img  # keep a reference
        unknown_button.grid(row=1, column=0)

        check_img = PhotoImage(file="images/right.png")
        known_button = Button(image=check_img, highlightthickness=0, command=on_mark_known)
        known_button.image = check_img  # keep a reference
        known_button.grid(row=1, column=1)

        self.flip_timer = window.after(3000, on_flip)

    def update_card(self, title, word, front=True):
        self.canvas.itemconfig(self.card_title, text=title, fill="black" if front else "white")
        self.canvas.itemconfig(self.card_word, text=word, fill="black" if front else "white")
        self.canvas.itemconfig(self.card_background, image=self.card_front_img if front else self.card_back_img)
