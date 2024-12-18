from quiz_util import questions, answers

score = 0
number_of_questions = len(questions)

def check_answer(score):
    for i in range(len(questions)):
        if float(input((questions[i]))) == answers[i]:
            score += 1
            print("Well done!")
        else:
            print(f"Nope, right answer was {answers[i]}...")
    return score



if __name__ == "__main__":
    print("Your result is: " + str(int((check_answer(score) / number_of_questions) * 100)) + "%")



