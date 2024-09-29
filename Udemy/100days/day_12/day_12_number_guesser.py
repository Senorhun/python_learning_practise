import random
print("Welcome to the Number Guessing Game!")
HARD_MODE = 10
EASY_MODE = 5

def setup():
    number_list = [number for number in range(1,101)]
    ai_num = random.choice(number_list)
    # ai_num = random.randint(1,100)
    return ai_num

def mode():
    mode = input("Choose difficulty: 'easy' or 'hard'\n")
    if mode == "easy":
        return HARD_MODE
    elif mode == "hard":
        return EASY_MODE
    
def guessing(life_count,ai_num):
    while True:
        user_num = int(input("Guess a number:  "))
        if user_num > ai_num:
            print("Too high...")
            life_count -= 1
        elif user_num < ai_num:
            print("Too low...")
            life_count -= 1
        elif user_num == ai_num:
            print("***Well done, your Won!***")
            break
        if life_count == 0:
            print(f"***Sorry, end of the game...number was {ai_num}***")
            break
        print(f"Guess again, still remain: {life_count} guesses.")

def game():
    ai_num = setup
    life_count = mode
    guessing(life_count(), ai_num())

if __name__ == "__main__":
    game()
