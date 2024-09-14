num = 12345
result = 0
for i in range(len(str(num))):
    result += num % 10
    num = int(num/10)
print(result)