def operate():
    x = 0
    option = None
    while True:
        if option == "n" or option =="c" or x < 1 or option != "t":
            if x < 1:
                result_list= [0,0,0,0]
            result_list = cont_calc(result_list[3], option, x)
            x += 1
        elif option == "t":
            print("Thank you for using our program!")
            break
        else:
            print("Please follow the instructions...")
        print(f"{result_list[0]} {result_list[1]} {result_list[2]} = {result_list[3]}")
        while True:
            option = input(f"Do you want to calculate (c) with number {result_list[3]} or start a new calculation (n) or terminate program (t) ?\n")
            if option in ["c","n","t"]:
                break
            else:
                print("Please follow instructions...")

def cont_calc(number, option, x):
    if option == "n" or x < 1:
        while True:
            num_1 = input("What is your first number?  ")
            if num_1.isdigit():
                num_1= int(num_1)
                break
            else:
                print("Please follow instructions...")
    elif option == "c":
        num_1 = number
    while True:
            operation = input("\n+\n-\n*\n/\nChoose an operation:  ")
            if operation in ["+","-","/","*"]:
                break
            else:
                print("Please follow instructions...")
    while True:
            num_2 = input("What is your second number?  ")
            if num_2.isdigit():
                num_2= int(num_2)
                break
            else:
                print("Please follow the instructions...")
    if operation == "+":
        return [num_1, "+", num_2, num_1 + num_2,]
    elif operation == "-":
        return [num_1, "-", num_2, num_1 - num_2,]
    elif operation == "*":
        return [num_1, "*", num_2, num_1 * num_2,]
    elif operation == "/":
        return [num_1, "/", num_2, num_1 / num_2,]
    else:
        print("Please follow the instructions...")

if __name__ == "__main__":
    print("Welcome to the calculator program!")
    operate()