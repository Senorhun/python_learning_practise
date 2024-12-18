def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b = temp + b
    return a

for i in range(10):
    print(i, fibonacci(i))


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(10):
    print(i, fibonacci(i))

