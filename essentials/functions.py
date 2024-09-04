
def greetings(name):
    print(f"Hello {name}!")
# greetings("Peter")


def greetings(name, nickname=None):
    if nickname == None:
        print(f"Hello, {name}!")
    else:
        print(f"Hello, {nickname}!")
# greetings("Peter","Senorhun")


def calculator(a, b, c=0):
    print(a + b + c)
#calculator(2, 3)




#----------------------------------------------------



from enum import Enum
class Basics(Enum):
    summ = 1
    mult = 2

def multiply(numbers):
    result = 1
    for _ in numbers:
        result *= _
    return result

#parameter = 1, 2, 3, 4
#print(multiply(parameter))

#parameter = (1, 2, 3, 4)
#print(multiply(parameter))

"""
def calculator(*args, calc = Basics.mult):
    if calc == Basics.summ:
        print(sum(args))
    elif calc == Basics.mult:
        print(multiply(args))

calculator(2, 3, 7, calc = Basics.summ)
calculator(2, 3, 7)
"""
def calculatorPlus(calc, *args):
    if isinstance(calc,int):
        calc = Basics(calc)
    if calc == Basics.summ:
        print(sum(args))
    elif calc == Basics.mult:
        print(multiply(args))

calculatorPlus(1,2,3)
calculatorPlus(2,2,3)

def dictionary(**kwargs):
    print(kwargs)
dictionary(name = "Peter", age = "34", cool = True)

x = "global variable"
def parameter_scope():
    global x 
    x = "inner variable"
    print(x)
parameter_scope()
print(x)

# if __name__ == "__main__":
