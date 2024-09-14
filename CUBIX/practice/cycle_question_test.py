questions = [
    "What is 2 + 2?  ",
    'What is "2" + "2"?  ',
    "What is 3 / 2?  ",
    "What is 3 // 2?  ",
    "What is 2 ** 3?  ",
]

answers = [
    4,
    22,
    1.5,
    1,
    8,
]

score = 0
number_of_questions = len(questions)
for i in range(len(questions)):
    if float(input((questions[i]))) == answers[i]:
        score += 1
        print("Well done!")
    else:
        print(f"Nope, right answer was {answers[i]}...")
print("Your result is: " + str(int((score / number_of_questions) * 100)) + "%")