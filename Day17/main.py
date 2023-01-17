from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import os

clear = lambda: os.system('cls')

question_bank = []

for data in question_data:
    new_question = Question(data['text'], data['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

clear()
while quiz.still_has_questions():
    quiz.next_question()

print("You have finished this quiz.")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")