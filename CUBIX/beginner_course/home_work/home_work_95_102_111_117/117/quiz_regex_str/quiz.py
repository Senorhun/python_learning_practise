import re
from quiz_util import question_bank

def check_answer(user_input, correct_answer):
    if re.match(correct_answer, user_input):
        return True
    return False

def quiz():
    score = 0
    for question in question_bank:
        user_input = input(f"\nHogy írják angolul hogy {question[0]}? ")
        if check_answer(user_input, question[1]):
            score += 1
            print("Szép volt, jár a piros pont :D")
        else:
            print("Ejnye, no...")
    return score

if __name__ == "__main__":
    result = quiz()
    print(f"\nElért pontszám {result} /{len(question_bank)}pont")
    print(f"Ez összesen {(result/len(question_bank)):.1%}")