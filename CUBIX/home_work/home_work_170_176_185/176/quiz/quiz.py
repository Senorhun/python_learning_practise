from xmlrpc.client import DateTime
from difflib import SequenceMatcher
from question_type import Question_type
import datetime



score = 0
questions_and_answers = []
number_of_questions = 0
path = "CUBIX/home_work/home_work_170_176_185/176/quiz/question.txt"


with open(path, mode='r') as file:
    for line in file:
        try:
            type, question, correct_answer = line.strip().split(',')
            if type.strip() == str(Question_type.MATH):
                correct_answer = float(correct_answer.strip())
            elif type.strip() == str(Question_type.DATE):
                correct_answer = datetime.date.fromisoformat(correct_answer.strip())
            else:
                correct_answer = correct_answer.strip()
            number_of_questions += 1
            questions_and_answers.append((type, question, correct_answer))
        except ValueError:
            print(f"Line in the file doesn't match the expected format and was skipped: {line.strip()}")

def check_answer(score):
    for type, question, correct_answer in questions_and_answers:
        user_answer = None
        if type == str(Question_type.MATH):
            while True:
                try:
                    user_answer = float(input(question+" "))
                    break
                except ValueError:
                    print("Please enter a number...")
        elif type == str(Question_type.TEXT):
            user_answer = input(question + " ") 
        elif type == str(Question_type.DATE):
            while True:    
                user_answer_unformatted = input(question + " ") 
                try:
                    user_answer = datetime.date.fromisoformat(user_answer_unformatted)
                    break
                except ValueError:
                    print("Please enter a valid date format YYYY-MM-DD...")
        if user_answer == correct_answer:
            score += 2
            print(f"Well done! +2points, Total score so far: {score}")
        else:
            print(f"Nope, right answer was {correct_answer}...")
            if type == str(Question_type.MATH):
                if abs(user_answer - correct_answer) <= correct_answer * 0.05:
                    score += 2
                    print(f"But close enough, Well done! +2points")
                elif abs(user_answer - correct_answer) <= correct_answer * 0.1:
                    score += 1
                    print(f"But close to have at least +1point")
                print(f"Total score so far: {score}")
                print(f"Difference is {round((abs(user_answer - correct_answer) / correct_answer* 100),2)}%")     
            elif correct_answer == str(Question_type.TEXT):
                if SequenceMatcher(None, user_answer, correct_answer).ratio() >= 0.6:
                    score += 1
                    print(f"But close to have at least +1point")
    return score

if __name__ == "__main__":

    if number_of_questions > 0:
            final_score = check_answer(score)
            print(f"\nYour final result is: {str(int((final_score / (number_of_questions * 2)) * 100))}%")
    else:
        print("No questions were found. Please check the question file.")

