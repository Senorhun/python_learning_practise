num = 12
print(type(num))
print(id(num))

a, b, c, d = 2, 3.14, "Hello World", [0,1,2,3,4]
print(type(a))
print(type(b))
print(type(c))
print(type(d))

number1 = pow(2,3)
number2 = pow(18,302)
number3 = pow(12232,34567) #ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
print(number1)
print(number2)
print(number3)

