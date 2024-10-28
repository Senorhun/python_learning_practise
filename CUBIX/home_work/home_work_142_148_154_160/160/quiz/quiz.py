from quiz_util import questions_and_answers
from difflib import SequenceMatcher
from question_type import Question_type

score = 0
number_of_questions = len(questions_and_answers)

def check_answer(score):
    for i in range(len(questions_and_answers)):
        if questions_and_answers[i][0] == Question_type.MATH:
            while True:
                try:
                    user_answer = float(input((questions_and_answers[i][1])))
                    break
                except ValueError:
                    print("Please enter a number...")
        elif questions_and_answers[i][0] == Question_type.TEXT:
            user_answer = input((questions_and_answers[i][1])) 
        if user_answer == questions_and_answers[i][2]:
            score += 2
            print(f"Well done! +2points, Total score so far: {score}")
        else:
            print(f"Nope, right answer was {questions_and_answers[i][2]}...")
            if questions_and_answers[i][0] == Question_type.MATH:
                if abs(user_answer - questions_and_answers[i][2]) <= questions_and_answers[i][2] * 0.05:
                    score += 2
                    print(f"But close enough, Well done! +2points")
                elif abs(user_answer - questions_and_answers[i][2]) <= questions_and_answers[i][2] * 0.1:
                    score += 1
                    print(f"But close to have at least +1point")
                print(f"Total score so far: {score}")
                print(f"Difference is {round((abs(user_answer - questions_and_answers[i][2]) / questions_and_answers[i][2]* 100),2)}%")     
            elif questions_and_answers[i][0] == Question_type.TEXT:
                if SequenceMatcher(None, user_answer, questions_and_answers[i][2]).ratio() >= 0.6:
                    score += 1
                    print(f"But close to have at least +1point")
    return score

if __name__ == "__main__":
    print(f"\nYour final result is: {str(int((check_answer(score) / (number_of_questions*2)) * 100))}%")



