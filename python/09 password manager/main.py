from tkinter import *
from tkinter import messagebox
import pandas
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_number + password_letters + password_symbols
    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    # use of join to convert list, tuple, dictionary of string to single string
    generated_password = "".join(password_list)
    pyperclip.copy(generated_password)
    password_input.delete(0, END)
    password_input.insert(0, generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_form(event=None):
    website_name = website_input.get().lower().capitalize()
    username_name = username_input.get()
    password = password_input.get()

    new_data = {
        website_name: {
            "email/username": username_name,
            "password": password
        }
    }
    # data = pandas.read_csv("password.csv")
    # website_list = data.website.tolist()

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Do not leave any thing blank ‼️")
        if len(website_name) == 0:
            website_input.focus()
        else:
            password_input.focus()

    # elif website_name.lower() in website_list:
    #     messagebox.showerror(title="Error", message="entered website name already exist 🧐")

    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"entered details are :\nEmail : "
                                                                   f"{username_name}\nWebsite : {website_name}\n"
                                                                   f"Password : {password}\nAre you sure to add?")
        if is_ok:
            try:
                with open("password.json", mode="r") as file:
                    # file.write(f"{website_name},{username_name},{password}\n")
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("password.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("password.json", mode="w") as file:
                    json.dump(data, file, indent=4)

            finally:
                messagebox.showerror(title="Done", message="new website password added successfully")
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
        else:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

# ---------------------------- search website  ------------------------------- #
# day 30 project

def search():
    s = website_input.get().lower().capitalize()
    trimmed_s = s.strip()
    try:
        with open("password.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Not found", message="The file is empty")
    else:
        if trimmed_s in data:
            messagebox.showerror(title="info",message=f"email/username : {data[trimmed_s]["email/username"]}\n"
                                                      f"password : {data[trimmed_s]["password"]}")
        else:
            messagebox.showerror(title="Not found", message=f"No details for {trimmed_s} available")
# ---------------------------- search website  ------------------------------- #


def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"


def focus_previous_widget(event):
    event.widget.tk_focusPrev().focus()
    return "break"


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website :", bg="white", foreground="black")
website_label.grid(column=0, row=1)

username_label = Label(text="email/username :", bg="white", foreground="black")
username_label.grid(column=0, row=2)

password_label = Label(text="password :", bg="white", foreground="black")
password_label.grid(column=0, row=3)

website_input = Entry(width=21, bg="white", highlightbackground="white", foreground="black", insertbackground="black", insertwidth=2)
website_input.focus()
website_input.grid(column=1, row=1, sticky=EW)

username_input = Entry(width=35, bg="white", highlightbackground="white", foreground="black", insertbackground="blue", insertwidth=2)
username_input.insert(0, "mdnurulhasan1111@gmail.com")
username_input.grid(column=1, row=2, columnspan=2, sticky=EW)

password_input = Entry(width=21, bg="white", highlightbackground="white", foreground="black", insertbackground="red", insertwidth=2)
password_input.grid(column=1, row=3, sticky=EW)

website_input.bind("<Return>", focus_next_widget)
username_input.bind("<Return>", focus_next_widget)
password_input.bind("<Return>", focus_next_widget)

website_input.bind("<Down>", focus_next_widget)
username_input.bind("<Down>", focus_next_widget)
password_input.bind("<Down>", focus_next_widget)

website_input.bind("<Up>", focus_previous_widget)
username_input.bind("<Up>", focus_previous_widget)
password_input.bind("<Up>", focus_previous_widget)

search_button = Button(text="search", highlightbackground="white", command=search)
search_button.grid(column=2, row=1, sticky=EW)

generate_password_button = Button(text="Generate Password", highlightbackground="white",
                                  command=generate_password)
generate_password_button.grid(column=2, row=3, sticky=EW)


password_input.bind("<Return>", save_form)
add_password_button = Button(text="Add password", width=36, highlightbackground="white", command=save_form)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
