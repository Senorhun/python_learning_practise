# number = int(input("Input a number to decide if its odd or even\n"))
# if number %2 == 0:
#     print("even")
# else:
#     print("odd")

print("welcome to python pizza delivery")
size = (input("Size: S M L\n")).upper()
pepperoni = (input("Pepperoni:\nYes(Y) or NO(N)\n")).upper()
extra_cheese = (input("Extra cheese:\nYes(Y) or NO(N)\n")).upper()

pizza_s = 15
pizza_m = 20
pizza_l = 25
pepperoni_s = 2
pepperoni_m_l = 3
extra_cheese_price = 1
result_price = 0

if size == "S":
    price = pizza_s
    if pepperoni == "Y":
        price += pepperoni_s
elif size == "M":
    price = pizza_m
    if pepperoni == "Y":
        price += pepperoni_m_l
elif size == "L":
    price = pizza_l
    if pepperoni == "Y":
        price += pepperoni_m_l
if extra_cheese == "Y":
    price += extra_cheese_price
print(f"pizza price is {price}")
