# fruits = [ "Apple","Peach","Pear"]
# for fruit in fruits:
#     print(fruit)

# student_scores = [150,142,185,120,171,184,149,24,59,68,199,78,65,89]
# total = sum(student_scores)
# print(total)

# sum = 0
# for number in student_scores:
#     sum += number
# print(sum)

# print(max(student_scores))

# biggest = 0
# for number in student_scores:
#     if number > biggest:
#         biggest = number
# print(biggest)

# for num in range(0,10,2):
#     print(num)

# sum = 0
# for num in range(1,101):
#     sum += num
# print(sum)

# for num in range(1,101):
#     if num % 3 == 0:
#         if num % 5 == 0:
#             print("FizzBuzz")
#         else:
#             print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)

from random import choice, randint, random, shuffle


letters = ['a','b','c','d','e','f','e','g','h','i','j','k','l','m','n','o','p','q','r','s','x','y','z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['#','%','*','!','+','=']

input_letter = int(input("How many letters would you like?  "))
input_numbers = int(input("How many numbers would you like?  "))
input_symbol = int(input("How many symbols would you like?  "))

pass_list = []
for i in range(0,input_letter):
    while True:
        letter = choice(letters)
        if letter not in pass_list:
            pass_list.append(letter)
            break
for i in range(0,input_numbers):
    while True:
        number = choice(numbers)
        if number not in pass_list:
            pass_list.append(number)
            break
for i in range(0,input_symbol):
    while True:
        symbol = choice(symbols)
        if symbol not in pass_list:
            pass_list.append(symbol)
            break
        
shuffle(pass_list)

result = ""
for i in pass_list:
    result += str(i)
print(result)