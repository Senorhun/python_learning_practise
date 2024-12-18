questions_and_answers= [
    (1,'What is the capital of Hungary? ','Budapest'),
    (1,'Which animal has trunk and long ears? ', 'elephant'),
    (2,'What celsius the water boils? ', 100),
    (1,'How do you say apple in hungarian? ', 'alma'),
    (1,'What is the first name of famous hungarian poet Petőfi? ', 'Sándor')
]

def ask_question(type, question, answer) -> bool:
    user_answer = input(question)
    if type == 1:
        if user_answer == answer:
            print('Well done!')
            return True
        else:
            print('Answer is wrong, solution is ' + answer)
            return False
    elif type == 2:
        user_answer_num = int(user_answer)
        if  user_answer_num == answer:
            print('Well done!')
            return True
        else:
            print('Answer is wrong, solution is ' + str(answer) + ', difference is: ' + str(answer-user_answer_num))
            return False

number_of_questions = 0
score = 0
for type, question, answer in questions_and_answers:
    number_of_questions += 1
    is_right = ask_question(type, question, answer)
    if is_right:
        score += 1

percent = str(100 * score / number_of_questions)
print('Result: ' + percent + '%')