def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a , b):
    return a / b

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def run_calc():
    while True:
            num_1 = input("What is your first number?  ")
            try:
                num_1= float(num_1)
                break
            except ValueError:
                print("Please follow instructions...")
    while True:
        while True:
            operandus = input("Choose operand\n+\n-\n*\n/\n")
            if operandus in ["+","-","/","*"]:
                break
            else:
                print("Please follow instructions...")
        while True:
            num_2 = input("What is your second number?  ")
            try:
                num_2= float(num_2)
                break
            except ValueError:
                print("Please follow the instructions...")
        result = operation[operandus](num_1,num_2)
        result_str = f"{num_1} {operandus} {num_2} = {result}"
        print(result_str)
        choice = input(f"Do you want to continue (c) with number {result} or start a new calculation (n) or terminate program (t) ?  ")
        if choice == "c":
            num_1 = result
        elif choice == "n":
            run_calc()
        elif choice == "t":
            print("Thank you for using our calculator, bye!")
            break

if __name__ == "__main__":
    run_calc()