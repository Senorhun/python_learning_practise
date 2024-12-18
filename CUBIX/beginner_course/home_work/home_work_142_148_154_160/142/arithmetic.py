def do_math(sign):
    sign_dict= {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    return sign_dict[sign]

def calculate(sign, a, b):
    return do_math(sign)(a, b)

    
print(calculate("+", 3, 2))
print(calculate("-", 3, 2))
print(calculate("*", 3, 2))
print(calculate("/", 3, 2))

