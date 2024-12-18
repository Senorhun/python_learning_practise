import re
from quiz_util import question_bank


def check_answer(user_input, pattern):
    if re.match(pattern, user_input):
        return True
    return False

def quiz():
    score = 0
    for question in question_bank:
        user_input = input(f"{question[0]}: ")
        if check_answer(user_input, question[1]):
            score += 1
            print("\nYaay, talált!!")
        else:
            print("\nNope...")
    
    print(f"\nElért pontszám: {score} /{len(question_bank)}pont\nEz összesen: {score/len(question_bank):.1%}")

if __name__ == "__main__":
    quiz()
