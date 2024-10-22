import re
from quiz_util import question_bank

class Quiz:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.score = 0

    def start_quiz(self):
        for question in self.question_bank:
            self.ask_question(question)

    def check_answer(self, user_input, correct_answer):
        return bool(re.match(correct_answer, user_input))
    
    def ask_question(self, question):
        user_input = input(f"\n{question[0]} ")
        if self.check_answer(user_input, question[1]):
            self.score += 1
            print("Szép volt, jár a piros pont :D")
        else:
            print("Ejnye, no...")

    def get_result(self):
        total_questions = len(self.question_bank)
        print(f"\nElért pontszám {self.score} / {total_questions} pont")
        print(f"Ez összesen {(self.score / total_questions):.1%}")

if __name__ == "__main__":
    quiz = Quiz(question_bank)
    quiz.start_quiz()
    quiz.get_result()
