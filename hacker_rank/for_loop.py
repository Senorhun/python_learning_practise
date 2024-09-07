def square_num(i):
    return i**2

if __name__== "__main__":
    n = int(input("Input a number for iteration to get the number's squares\n"))
    for i in range(n):
        print(square_num(i))