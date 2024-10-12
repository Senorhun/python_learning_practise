from quiz_util import questions_and_answers

def check_answer(type, answer, correct_answer):
    answer = input(question + ' ')
    if type == 2:
        if answer == correct_answer:
            return True, 'Well done!', 1, False
        else:
            return False, 'Nope...correct answer: ' + str(correct_answer), 0, False
    elif type == 1:
        answer_num = float(answer)
        if answer_num == correct_answer:
            return True, 'Well done!', 2, False
        else:
            if abs(answer_num - correct_answer) <= correct_answer * 0.1:
                return False, 'Nope, but close...correct answer: ' + str(correct_answer) + ' Difference: ' + str(abs(round(answer_num - correct_answer,2))), 1, True

            return False, 'Nope...correct answer: ' + str(correct_answer) + ' Difference: ' + str(abs(round(answer_num - correct_answer,2))), 0, False

num_of_question = 0
score = 0
for type, question, correct_answer in questions_and_answers:
    num_of_question += 2
    is_correct, str_answer, point, is_half = check_answer(type, question, correct_answer)
    print("Answer is: ", is_correct, ", " + str_answer, "reward: +" + str(point) + "point")
    if is_correct:
        score += 2
    elif is_half:
        score += 1

percent = str(round(100 * score / num_of_question,1))
print('Result: ' + percent + '%')
