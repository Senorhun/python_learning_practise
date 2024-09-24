from quiz_util import questions_and_answers


score = 0
number_of_questions = len(questions_and_answers)

def check_answer(score):
    for i in range(len(questions_and_answers)):
        if questions_and_answers[i][0] == 1:
            user_answer = float(input((questions_and_answers[i][1])))
        elif questions_and_answers[i][0] == 2:
            user_answer = input((questions_and_answers[i][1])) 
        if user_answer == questions_and_answers[i][2]:
            score += 2
            print("Well done! +2points")
        else:
            print(f"Nope, right answer was {questions_and_answers[i][2]}...")
            if questions_and_answers[i][0] == 1:
                if abs(user_answer - questions_and_answers[i][2]) <= questions_and_answers[i][2] * 0.1:
                    score += 1
                    print("But close, so +1point!")
                print(f"Difference is {round((abs(user_answer - questions_and_answers[i][2]) / questions_and_answers[i][2]* 100),2)}%")     
    return score

if __name__ == "__main__":
    print("Your result is: " + str(int((check_answer(score) / (number_of_questions*2)) * 100)) + "%")



