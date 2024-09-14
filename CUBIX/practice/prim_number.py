number = int(input("Input a number  "))

counter = 0
for i in range(2,number+1):
    if number % i == 0:
        counter += 1
if counter == 1:
    print(f"{number} is a prim")
else:
    print(f"{number} is NOT a prim")


print("------------")


import math

number = int(input("Input a number: "))

if number < 2:
    print(f"{number} is NOT a prime")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime")
    else:
        print(f"{number} is NOT a prime")

print("-------------------")

number = int(input("Input a number: "))

if number < 2:
    print(f"{number} is NOT a prime")
else:
    is_prime = True
    i = 2
    while i * i <= number:
        if number % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(f"{number} is a prime")
    else:
        print(f"{number} is NOT a prime")
