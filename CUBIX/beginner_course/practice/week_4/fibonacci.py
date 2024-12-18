# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         temp = a
#         a = b
#         b = temp + b
#     return a

# for i in range(10):
#     print(i, fibonacci(i))



def fibonacci(n):
    fibonacci_num = (n+1) * [None]
    def fibonacci_recursive(x):
        if fibonacci_num[x] is None:
            fibonacci_num[x] = x if x <= 1 else fibonacci_recursive(x-1) + fibonacci_recursive(x-2)             
        return fibonacci_num[x] 
        
    return fibonacci_recursive(n)

    
for i in range(50):
    print(i, fibonacci(i))

