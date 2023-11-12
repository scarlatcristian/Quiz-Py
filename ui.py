from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text='Score: 0', fg='white',
                           highlightthickness=0, borderwidth=0, bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 125, text='Some question', fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file='./images/true.png')
        false_img = PhotoImage(file='./images/false.png')

        self.true_btn = Button(
            image=true_img, highlightthickness=0, borderwidth=0)
        self.true_btn.grid(row=2, column=0)

        self.false_btn = Button(
            image=false_img, highlightthickness=0, borderwidth=0)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()
