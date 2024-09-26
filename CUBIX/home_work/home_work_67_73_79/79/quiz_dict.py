import random
history_date = {
    'Hungarian Revolution and Freedom Fight':'1956',
    'Signing of the Magna Carta':'1215',
    'Columbus Discovers America':'1492',
    "Martin Luther's 95 Theses":'1517',
    'American Declaration of Independence':'1776',
    'French Revolution Begins':'1789',
    'Emancipation Proclamation':'1863',
    'End of World War I':'1918',
    'Moon Landing (Apollo 11)':'1969',
    'Fall of the Berlin Wall ':'1989',
}
number_of_questions = 5
number_of_choices = 3
score = 0
for event in random.sample(list(history_date),number_of_questions):
    correct_answer = history_date[event]
    wrong_answers = list(history_date.values())
    wrong_answers.remove(correct_answer)
    choices = random.sample((wrong_answers),number_of_choices-1)
    choices.append(correct_answer)
    choices.sort()
    choices_dict = {chr(ord('A') +i) : choices[i] for i in range(number_of_choices)}
    print(f"What year {event} happened?  ")
    for letter, capital in choices_dict.items():
        print("    " + letter + ": " + capital)
    user_answer = input("Choose-> A, B, C:   ").upper()
    if correct_answer == choices_dict[user_answer]:
        print("Correct, well done +1 point!")
        score += 1
    else:
        print(f"nooope cuz it's {correct_answer}")
    print(f"Score: {score}/5")
print(f"End of test: {((score / number_of_questions) *100)}%")


 
