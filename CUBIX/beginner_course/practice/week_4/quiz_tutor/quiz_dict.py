import random
country_capitals = {
    'Albánia':'Tirana',
    'Andorra':'Andorra la Vella',
    'Ausztria':'Bécs',
    'Belgium':'Brüsszel',
    'Bosznia-Hercegovina':'Szarajevó',
    'Bulgária':'Szófia',
    'Csehország':'Prága',
    'Dánia':'Koppenhága',
    'Egyesült Királyság':'London',
    'Észtország':'Tallin',
}
number_of_questions = 5
number_of_choices = 4
score = 0
for country in random.sample(list(country_capitals),number_of_questions):
    correct_answer = country_capitals[country]
    wrong_answers = list(country_capitals.values())
    wrong_answers.remove(correct_answer)
    choices = random.sample((wrong_answers),number_of_choices-1)
    choices.append(correct_answer)
    random.shuffle(choices)
    choices_dict = {chr(ord('A') +i) : choices[i] for i in range(number_of_choices)}
    print(f"What is the capital of {country}?  ")
    for letter, capital in choices_dict.items():
        print("    " + letter + ": " + capital)
    user_answer = input("Choose-> A, B, C, D:   ").upper()
    if correct_answer == choices_dict[user_answer]:
        print("correct")
        score += 1
    else:
        print(f"nooope cuz it's {correct_answer}")
print(f"Score: {score}/5 -> {((score / number_of_questions) *100)}%")


 
