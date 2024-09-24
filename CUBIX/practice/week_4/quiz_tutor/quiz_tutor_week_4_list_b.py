questions_and_answers= [
    ('What is the capital of Hungary? ','Budapest'),
    ('Which animal has trunk and long ears? ', 'elephant'),
    ('What celsius the water boils? ', '100'),
    ('How do you say apple in hungarian? ', 'alma'),
    ('What is the first name of famous hungarian poet Petőfi? ', 'Sándor')
]


def ask_question(question: str, answer: str) -> bool:
    user_answer = input(question)
    if user_answer == answer:
        print('Well done!')
        return True
    else:
        print('Answer is wrong, solution is ' + answer)
        return False

number_of_questions = 0
score = 0
for question, answer in questions_and_answers:
    number_of_questions += 1
    is_right = ask_question(question, answer)
    if is_right:
        score += 1

percent = str(100 * score / number_of_questions)
print('Result: ' + percent + '%')