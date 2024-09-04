print("---1-----")


def add(number):
    return number + 10


print(add(1))

print("---2-----")

add_lambda = lambda a: a + 1
print(add_lambda(10))

print("---3-----")

x = lambda x: x * 1.5
print(x(20))

print("---4-----")

y = lambda y: y / 3
print(y(20))
