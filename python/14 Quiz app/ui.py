from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class UserInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        # self.score = 0
        self.timer = None
        self.user_input: str = "True"
        self.window.title("Quiz")
        # window.minsize(width=600, height=500)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"score : {self.quiz.score}", font=("Courier", 20, "normal"), foreground="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(bg="white", highlightthickness=0)
        self.title_label = self.canvas.create_text(150, 130, width=280, anchor="center", text="Hello", fill="black")

        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.cross_img = PhotoImage(file="./images/false.png")
        self.cross_button = Button(image=self.cross_img, highlightthickness=0, highlightbackground=THEME_COLOR,
                                   command=self.cross_input)
        # cross_button.grid(column=0, row=1, sticky=W)
        # this is a good way than using sticky
        self.cross_button.grid(column=0, row=2)

        self.tick_img = PhotoImage(file="./images/true.png")
        self.tick_button = Button(image=self.tick_img, highlightthickness=0, highlightbackground=THEME_COLOR,
                                  command=self.tick_input)
        # tick_button.grid(column=0, row=1, sticky=E)
        self.tick_button.grid(column=1, row=2)
        self.next_question()

        self.exit_button = Button(text="Exit", highlightthickness=0,
                                  highlightbackground=THEME_COLOR, command=self.window.destroy)
        self.exit_button.grid(column=0, row=3, columnspan=3, pady=20, sticky="ew")

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white", highlightthickness=0)
        if self.quiz.still_has_questions() != 10:
            q_text = self.quiz.next_question()

            # Create the text at the center position using the 'center' anchor
            # self.canvas.delete(self.title_label)
            # self.canvas.create_text(x, y, text=q_text, anchor='center', fill="black", width=280)
            self.canvas.itemconfig(self.title_label, text=q_text, anchor='center', fill="black", width=280)
            self.canvas.config(bg="white", highlightthickness=0)
        else:
            self.quiz.question_number += 1
            self.canvas.itemconfig(self.title_label, text=f"Quiz completed\n", anchor='center', fill="black",
                                   width=280, font=("Courier", 30, "bold"))
            self.canvas.create_text(150, 200, text=f"final score : {self.quiz.score}/10", font=("Courier", 20, "normal"), fill="black")

    def tick_input(self):
        # self.next_question()
        self.user_input = "True"
        self.check_answer()
        self.window.after(1000, self.perform_action)
        self.tick_button.config(state=DISABLED)

    def cross_input(self):
        # self.next_question()
        self.user_input = "False"
        self.check_answer()
        self.window.after(1000, self.perform_action)
        self.cross_button.config(state=DISABLED)

    def perform_action(self):
        if self.quiz.still_has_questions() != 11:
            self.tick_button.config(state=NORMAL)
            self.cross_button.config(state=NORMAL)
        else:
            self.tick_button.config(state=DISABLED)
            self.cross_button.config(state=DISABLED)

    def check_answer(self):
        is_correct = self.quiz.check_answer(user_answer=self.user_input)
        if is_correct:
            self.canvas.config(bg="green", highlightthickness=0)
            self.score_label.config(text=f"score : {self.quiz.score}")
        else:
            self.canvas.config(bg="red", highlightthickness=0)
        self.timer = self.window.after(1000, self.next_question)

