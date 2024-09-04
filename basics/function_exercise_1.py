year = None

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year!') 
            else:
                print(f'{year} is NOT a leap year!') 
        else:
            print(f'{year} is a leap year!')
    else:
        print(f'{year} is NOT a leap year...')

def leapDecider():
    isLeapYear(1994),
    isLeapYear(2000),
    isLeapYear(1816),
    isLeapYear(2001)

year = int(input('Input a year and see if it\'s leap or not: '))
isLeapYear(year)

leapDecider()
    