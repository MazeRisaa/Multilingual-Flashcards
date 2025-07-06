from tkinter import *
import pandas
import random
import os
from ui import FlashcardUI

BACKGROUND_COLOR = "#B1DDC6"

class FlashcardApp:
    def __init__(self):
        # Load chosen languages
        with open("language_config.txt", "r", encoding="utf-8") as f:
            self.source_lang, self.target_lang = f.read().strip().split(",")

        base_csv_path = f"data/{self.source_lang.lower()}_{self.target_lang.lower()}_dictionary_fixed.csv"
        self.progress_path = f"progress/words_to_learn_{self.source_lang.lower()}_{self.target_lang.lower()}.csv"

        # Create progress folder if it doesn't exist
        os.makedirs("progress", exist_ok=True)

        try:
            self.data = pandas.read_csv(self.progress_path)
            print(f"Loaded saved progress from {self.progress_path}")
        except FileNotFoundError:
            self.data = pandas.read_csv(base_csv_path)
            print(f"No saved progress found. Loaded full dictionary from {base_csv_path}")

        self.to_learn = self.data.to_dict(orient="records")
        self.current_card = {}

        self.window = Tk()
        self.window.title("Flashcard App")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.card_front_img = PhotoImage(file="images/card_front.png")
        self.card_back_img = PhotoImage(file="images/card_back.png")

        self.ui = FlashcardUI(
            self.window,
            self.card_front_img,
            self.card_back_img,
            self.flip_card,
            self.mark_as_known,
            self.next_card
        )

        self.next_card()
        self.window.mainloop()

    def next_card(self):
        self.window.after_cancel(self.ui.flip_timer)
        self.current_card = random.choice(self.to_learn)
        self.ui.update_card(self.source_lang, self.current_card["Source Word"], front=True)
        self.ui.flip_timer = self.window.after(3000, self.flip_card)

    def flip_card(self):
        self.ui.update_card(self.target_lang, self.current_card["Translated Word"], front=False)

    def mark_as_known(self):
        self.to_learn.remove(self.current_card)
        pandas.DataFrame(self.to_learn).to_csv(self.progress_path, index=False)
        self.next_card()
