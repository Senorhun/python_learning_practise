
print("Welcome to the basic math test!")
number_of_questions = 5
result = 0
if (int(input("What is 2 + 2?  "))) == 4:
    result += 1
if (int(input('What is "2" + "2"?  '))) == 22:
    result += 1
if (float(input("What is 3 / 2?  "))) == 1.5:
    result += 1
if (int(input("What is 3 // 2?  "))) == 1:
    result += 1
if (int(input("What is 2 ** 3?  "))) == 8:
    result += 1
print("Your result is: " + str((result / number_of_questions)*100) + "%")

print("----------------------------")

year = (int(input("Was there a winter olympic game in the year: ")))
is_winter_olympic = (1924 <= year <= 1992 and year % 4 == 0 and year != 1940 and year != 1944) or (1994 <= year <= 2022 and year % 4 == 2)
print(is_winter_olympic)


