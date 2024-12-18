def print_hello(name = "World"):
    if name:
        print(f"Hello, {name}!")

print_hello()
print_hello("Peter")

print("---")

def summ(a,b):
    return a + b
def plus1(a: int, b=1) -> int:
    return a + b

print(summ(1,3))
print(plus1(5))