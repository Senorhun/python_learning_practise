from enum import Enum

class Month(Enum):
    JANUARY = 31
    FEBRUARY = 28
    MARCH = 31
    APRIL = 30
    MAY = 31
    JUNE = 30
    JULY = 31
    AUGUST= 31
    SEPTEMBER = 30
    OCTOBER = 31
    NOVEMBER = 30
    DECEMBER = 31

user_input = input("Pick a month to find out, how many days does it long:  ").upper()
try:
    match user_input:
        case "FEBRUARY":
            print(f"{user_input} is 28/29 days long depends on the year")
        case _:
            print(f"{user_input} is {Month[user_input].value} days long")
except KeyError:
    print("The month does not exist...")