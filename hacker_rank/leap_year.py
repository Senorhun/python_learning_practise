def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

if __name__ == "__main__":
    year = int(input("input a year to decide if its leap\n"))
    print(is_leap(year))