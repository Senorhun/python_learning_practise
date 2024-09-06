# print("Hello"[4])

# print(12345)
# print(12_345)

# print(5/3)
# print(5//3)
# print(2**3)

# weight = 78.7
# height = 1.76
# bmi = weight / (height**2)
# print(round(bmi))
# print(round(bmi, 2))

print("Welcome to the tip calculator!")
bill = float((input("What was the total bill?\n")))
tip = 0.01 * (float(input("How much tip would you like to give?\n10%\n12%\n15%\n")))
ppl = float(input("How many peaople will split the bill?\n"))
result = round((bill + (bill * tip)) / ppl, 2)
print(f"Each person should pay: ${result}")