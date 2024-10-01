from data import question_data
from question_model import Question
from quiz_brain import QuizBran

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBran(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")