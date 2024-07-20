import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
work = ""
# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(title_label, text="00:00")
    timer_label.config(text="Timer", foreground=GREEN)
    global work
    work = ""
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        window.config(padx=50)
        timer_label.config(text="Break", foreground=GREEN)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        window.config(padx=50)
        timer_label.config(text="Break", foreground=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text="work", foreground=RED)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    min_count = math.floor(count / 60)
    if min_count < 10:
        min_count = f"0{min_count}"
    # this is important here we should not put math.floor else would create glitch in the second part.
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"

    # if int(sec_count) < 10:
    #     sec_count = "0" + str(sec_count)

    canvas.itemconfig(title_label, text=f"{min_count}:{sec_count}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global work
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            work += "✅"
        check_label.config(text=work)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
# window.minsize(width=600, height=500)
window.config(bg=YELLOW, padx=100, pady=50)
timer_label = Label(text="Timer", font=(FONT_NAME, 55, "normal"))
timer_label.config(bg=YELLOW, foreground=GREEN)
timer_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.config(bg=YELLOW, highlightthickness=0)
title_label = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# count_down(5)

star_button = Button(text="start", command=start_timer)
star_button.config(bg=YELLOW, highlightthickness=0, highlightbackground=YELLOW)
star_button.grid(column=0, row=2)

reset_button = Button(text="reset", command=timer_reset)
reset_button.config(bg=YELLOW, highlightthickness=0, highlightbackground=YELLOW)
reset_button.grid(column=2, row=2)

check_label = Label(bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
