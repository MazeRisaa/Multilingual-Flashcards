from tkinter import *

def choose_language():
    def update_target_options(*args):
        # Rebuild target menu to exclude the source language
        selected_source = source_var.get()
        new_options = [lang for lang in languages if lang != selected_source]

        target_menu['menu'].delete(0, 'end')
        for option in new_options:
            target_menu['menu'].add_command(label=option, command=lambda value=option: target_var.set(value))

        # Set default target if it was the same as source
        if target_var.get() == selected_source:
            target_var.set(new_options[0])

    def start():
        src = source_var.get()
        tgt = target_var.get()
        if src == tgt:
            error_label.config(text="Languages must be different.", fg="red")
            return
        with open("language_config.txt", "w", encoding="utf-8") as f:
            f.write(f"{src},{tgt}")
        selector.destroy()

    selector = Tk()
    selector.title("Select Language Pair")
    selector.geometry("800x526")
    selector.config(padx=50, pady=50, bg="#B1DDC6")

    title_font = ("Ariel", 30, "bold")
    label_font = ("Ariel", 16)
    button_font = ("Ariel", 14, "bold")

    # Title
    Label(selector, text="Choose Languages", font=title_font, bg="#B1DDC6").pack(pady=40)

    languages = ["Arabic", "English", "French", "German", "Hungarian"]

    frame = Frame(selector, bg="#B1DDC6")
    frame.pack()

    Label(frame, text="From:", font=label_font, bg="#B1DDC6").grid(row=0, column=0, padx=20, pady=10)
    source_var = StringVar(value="English")
    OptionMenu(frame, source_var, *languages).grid(row=0, column=1, padx=20, pady=10)

    Label(frame, text="To:", font=label_font, bg="#B1DDC6").grid(row=1, column=0, padx=20, pady=10)
    target_var = StringVar(value="French")
    target_menu = OptionMenu(frame, target_var, *[lang for lang in languages if lang != source_var.get()])
    target_menu.grid(row=1, column=1, padx=20, pady=10)

    # Update target options dynamically
    source_var.trace_add("write", update_target_options)

    Button(selector, text="Start Flashcards", font=button_font, command=start, bg="#88c9a1", width=18).pack(pady=30)

    error_label = Label(selector, text="", bg="#B1DDC6", font=("Ariel", 12, "italic"))
    error_label.pack()

    selector.mainloop()
