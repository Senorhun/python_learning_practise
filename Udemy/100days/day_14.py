people = [
    {"name": "Elon Musk", "followers": 150_000_000, "occupation": "Entrepreneur", "country": "USA"},
    {"name": "Cristiano Ronaldo", "followers": 600_000_000, "occupation": "Footballer", "country": "Portugal"},
    {"name": "Taylor Swift", "followers": 300_000_000, "occupation": "Singer", "country": "USA"},
    {"name": "Lionel Messi", "followers": 450_000_000, "occupation": "Footballer", "country": "Argentina"},
    {"name": "Kylie Jenner", "followers": 400_000_000, "occupation": "Entrepreneur", "country": "USA"},
    {"name": "Dwayne Johnson", "followers": 350_000_000, "occupation": "Actor", "country": "USA"},
    {"name": "Kim Kardashian", "followers": 360_000_000, "occupation": "Media Personality", "country": "USA"},
    {"name": "Selena Gomez", "followers": 430_000_000, "occupation": "Singer/Actress", "country": "USA"},
    {"name": "Shakira", "followers": 130_000_000, "occupation": "Singer", "country": "Colombia"},
    {"name": "Neymar Jr.", "followers": 210_000_000, "occupation": "Footballer", "country": "Brazil"},
    {"name": "LeBron James", "followers": 160_000_000, "occupation": "Basketball Player", "country": "USA"},
    {"name": "Bill Gates", "followers": 60_000_000, "occupation": "Entrepreneur", "country": "USA"},
    {"name": "Rihanna", "followers": 140_000_000, "occupation": "Singer", "country": "Barbados"},
    {"name": "Barack Obama", "followers": 130_000_000, "occupation": "Politician", "country": "USA"},
    {"name": "Virat Kohli", "followers": 250_000_000, "occupation": "Cricketer", "country": "India"},
    {"name": "Ariana Grande", "followers": 380_000_000, "occupation": "Singer", "country": "USA"},
    {"name": "Katy Perry", "followers": 100_000_000, "occupation": "Singer", "country": "USA"},
    {"name": "Zendaya", "followers": 180_000_000, "occupation": "Actress", "country": "USA"},
    {"name": "Emma Watson", "followers": 80_000_000, "occupation": "Actress", "country": "UK"},
    {"name": "Roger Federer", "followers": 40_000_000, "occupation": "Tennis Player", "country": "Switzerland"}
]

import random 


def question():
    score = 0
    options = random.sample(people,2)
    option_1 = options[0]
    while True:
        options = random.sample(people,2)
        option_2 = options[1]
        option_1_str = (f"Compare A: {option_1["name"]} whose occupation is {option_1["occupation"]} who is from {option_1["country"]} \n")
        option_2_str = (f"Against B: {option_2["name"]} whose occupation is {option_2["occupation"]} who is from {option_2["country"]} ")
        print(option_1_str)
        print(option_2_str)
        print(f"Score: {score}")

        user_choice = None
        user_input = input("Who has more followers: A or B\n").upper()
        if user_input == "A":
            user_choice = option_1
        elif user_input == "B":
            user_choice = option_2
        result = validation(option_1, option_2)
        if result == user_choice:
            option_1 = result
            score += 1
        else:
            print(f"End of the game it was {result["name"]}, score: {score}")
            break
    
def validation(option_1, option_2):
    if option_1["followers"] > option_2["followers"]:
        winner = option_1
    else:
        winner = option_2
    return winner

if __name__ == "__main__":
    question()
