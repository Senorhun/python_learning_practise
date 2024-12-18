questions = [
    'What is the capital of Hungary? ',
    'Which animal has trunk and long ears? ',
    'What celsius the water boils? ',
    'How do you say apple in hungarian? ',
    'What is the first name of famous hungarian poet Petőfi? '
]
answers = [
    'Budapest',
    'elephant',
    '100',
    'alma',
    'Sándor',
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
for i in range(len(answers)):
    number_of_questions += 1
    is_right = ask_question(questions[i], answers[i])
    if is_right:
        score += 1

percent = str(100 * score / number_of_questions)
print('Result: ' + percent + '%')