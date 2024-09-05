def simple_generator():
    yield 1
    yield 2
    yield 3
gen = simple_generator()

for x in gen:
    print(x)

print(next(gen))
print(next(gen))
print(next(gen))

print("---------------")

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
x = fib(5)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))