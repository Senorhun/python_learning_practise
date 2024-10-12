
def sum(num1, num2):
    result = num1 + num2
    rounded_result = round(result,0)
    is_rounded = False
    difference = round(result -rounded_result, 3)
    if difference > 0:
        is_rounded = True
    return rounded_result, difference, is_rounded

if __name__ == "__main__":
    print("Welcome, let's sum two numbers!")
    try:
        num1_input, num2_input = float(input("Enter first number: ")), float(input("Enter second number: "))
        rounded_result, difference, is_rounded = sum(num1_input,num2_input)
        result = f"Result of sum {num1_input} and {num2_input} is {rounded_result}, function rounded result: {is_rounded} "
        if difference > 0:
            result += (f"Result was rounded by {difference}")
        print(result)
    except ValueError:
        print("Input is not valid...")