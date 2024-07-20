from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ----------------------- PICK WORD FROM DATA  -----------------------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient="records")

# using orient inside dict to change the default conversion to dictionary.
else:
    data_dict = data.to_dict(orient="records")
# print(random.choice())


def next_card():
    global timer
    global current_card
    window.after_cancel(timer)
    current_card = random.choice(data_dict)
    french_word = current_card["French"]
    english_word = current_card["English"]
    # canvas.create_text.config() random.choice(data_dict["French"])
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(canvas_text_main, text=french_word, font=("Arial", 80, "bold"), fill="black")
    canvas.itemconfig(canvas_text_title, text="French", font=("Arial", 40, "italic"), fill="black")
    timer = window.after(3000, english_card)
    # try:
    #     with open(file="memorised_word.csv", mode="a") as file:
    #         file.write(f"{french_word},{english_word}\n")
    # except FileNotFoundError:
    #     with open(file="memorised_word.csv", mode="w") as file:


def english_card():
    english_word = current_card["English"]
    #  PhotoImage won't work inside any function.
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(canvas_text_title, text="English", fill="white", font=("Arial", 40, "italic"))
    canvas.itemconfig(canvas_text_main, text=english_word, fill="white", font=("Arial", 80, "bold"))


def tick_got_clicked():
    french_word = current_card["French"]
    english_word = current_card["English"]
    data_dict.remove(current_card)
    print(len(data_dict))
    updated_data_dict = pandas.DataFrame(data_dict)
    updated_data_dict.to_csv("./data/words_to_learn.csv", index=False)
    try:
        with open(file="./data/memorised_word.csv", mode="a") as file:
            file.write(f"{french_word},{english_word}\n")

    except FileNotFoundError:
        with open(file="./data/memorised_word.csv", mode="w") as file:
            file.write(f"French,English\n")
        with open(file="./data/memorised_word.csv", mode="a") as file:
            file.write(f"{french_word},{english_word}\n")

    next_card()
# ----------------------- PICK WORD FROM DATA END-----------------------


# ----------------------- UI SETUP -----------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.after(3000, english_card)
timer = window.after(3000, english_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 270, image=front_img)
canvas_text_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "normal"), fill="black")
canvas_text_main = canvas.create_text(400, 263, text="word", font=("Arial", 60, "normal"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)
# canvas.pack()

cross_img = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
# cross_button.grid(column=0, row=1, sticky=W)
# this is a good way than using sticky
cross_button.grid(column=0, row=1)

tick_img = PhotoImage(file="./images/right.png")
tick_button = Button(image=tick_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=tick_got_clicked)
# tick_button.grid(column=0, row=1, sticky=E)
tick_button.grid(column=1, row=1)

next_card()

window.mainloop()

# ----------------------- UI SETUP END -----------------------
