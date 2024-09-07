def print_sequence(n):
    start = 1
    num_list = ""
    while start <= n:
        num_list += str(start)
        start +=1
    return num_list

if __name__ == "__main__":
    n = int(input("Input a number\n"))
    print(print_sequence(n))