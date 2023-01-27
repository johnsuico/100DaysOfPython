from tkinter import *
import os
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

# Setting up file paths
dirname = os.path.dirname(__file__)
false_img_path = os.path.join(dirname, './images/false.png')
true_img_path = os.path.join(dirname, './images/true.png')

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text='Score: 0', bg=THEME_COLOR, font=('arial', 12, 'normal'), fg='white')
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text='Test question text', font=('Arial', 16, 'italic'), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_img = PhotoImage(file=false_img_path)
        true_img = PhotoImage(file=true_img_path)

        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.set_user_ans_true)
        self.true_btn.grid(column=0, row=2)

        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.set_user_ans_false)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have finished this quiz.')
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def set_user_ans_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def set_user_ans_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)