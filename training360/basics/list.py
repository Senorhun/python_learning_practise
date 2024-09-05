numList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(len(numList))
numList.append("a")
print(numList)
numList.pop()
print(numList)

result = []

for num in numList:
    result.append(num)
    result.append("x")
print(result)

resultBuiltIn = list(numList)
print(resultBuiltIn)

sumNumList = [1, 2, 3]
print("result: ", sum(sumNumList))

a = [1, 2, 3]
b = [4, 5]
# c = a + b
#print(c)

a.extend(b)
print(a)

a.insert(3,9)
print(a)

a.sort()
print(a)

a.reverse()
print(a)