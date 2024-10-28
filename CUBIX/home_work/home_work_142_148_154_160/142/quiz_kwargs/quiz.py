import re
from quiz_util import question_bank

def check_answer(user_input, correct_answer):
    return bool(re.match(correct_answer, user_input))

def quiz(**kwargs):
    language = kwargs.get("selected_language", "angol")
    give_feedback = kwargs.get("is_feedback", False)
    score = 0
    for item in question_bank:
        correct_answer = item.get(language)
        if not correct_answer:
            print(f"No translation available for '{language}' for the word '{item['question']}'")
            continue
        user_input = input(f"\nHogy írják {language}ul azt, hogy '{item['question']}'? ")
        if check_answer(user_input, correct_answer):
            score += 1
            if give_feedback:
                print("Szép volt, jár a piros pont :D")
        else:
            if give_feedback:
                print("Ejnye, no...")
    return score

if __name__ == "__main__":
    selected_language = input("Which language do you want to answer in? (angol, német, spanyol): ")
    feedback_choice = input("Do you want feedback? (yes): ")
    is_feedback = feedback_choice == "yes"
    result = quiz(language = selected_language, is_feedback = is_feedback)
    print(f"\nElért pontszám {result} / {len(question_bank)} pont")
    print(f"Ez összesen {(result / len(question_bank)):.1%}")
