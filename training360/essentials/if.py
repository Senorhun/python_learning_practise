"""
from random import randint

num = int(input("Guess a number between 1-10:  "))
message = "It's a hit!" if num == randint(1,11) else "Not this time!"
print(message)
"""

num = 3

if num == 1:
    print("one")
elif num == 2:
    print("two")
elif num == 3:
    print("three")
else:
    print("no number was found")