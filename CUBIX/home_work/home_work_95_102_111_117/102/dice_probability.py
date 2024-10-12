def dice_probability(num):
    if num < 2 or num > 12:
        return "Input must be between 2 and 12."
    
    outcomes = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    matching_outcomes = [outcome for outcome in outcomes if sum(outcome) == num]
    probability = len(matching_outcomes) / 36
    return f"The probability of rolling a {num} is {probability:.2%}"

if __name__ == "__main__":
    user_input = int(input("Enter a number between 2 and 12: "))
    print(dice_probability(user_input))
