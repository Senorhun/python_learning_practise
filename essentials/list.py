list0 = ["a", "b", "c", "d", "e"]
print(list0[3])

list0 = ["a", "b", "c", "d", "e"]
list0.reverse()
print(list0)

list0 = ["a", "b", "c", "d", "e"]
print(list0[::-1])

print("---------------")

list0 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list0_new = []

for num in list0:
    if num > 30:
        list0_new.append(num)
print(list0_new)
print(list0)

print("-------list comprehension--------")

list0_new = [elem for elem in list0 if elem > 30]
print(list0_new)

print("---------------")
list0 = [10, 20, 30, 40, 50, 60, 70]
print(list0)
print(list0.pop())
print(list0)

print("---------------")
list0 = [10, 20, 30, 40, 50, 60, 70]
for index, elem in enumerate(list0):
    print(f"index: {index}  element: {elem}")

print("---------------")
for x in range(10):
    print(x)

print("---------------")
for x in range(5, 10):
    print(x)

print("---------------")
for x in range(3, 10, 2):
    print(x)

print("---------------")
for x in range(5, 10):
    print(x)
    if x == 8:
        break
else:
    print(f"finished")

print("---------------")
x = 1
while x < 10:
    print(x)
    x += 1

print("---------------")
names = ["Peter", "Andrea", "David"]
name1, name2, name3 = names
print(name1, name2, name3)
print(name1)

print("---------------")
text1 = "Morgen"
text2 = "Morgen"

isSame = True

if len(text1) != len(text2):
    isSame = False
else:
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            isSame = False
            break
print(isSame)

print("---------------")
text1 = "Morgen"
text2 = "Morgen"

if len(text1) != len(text2):
    isSame = False
else:
    for text1, text2 in zip(text1, text2):
        print(f"text1: {text1}   text2: {text2}")
        if text1 != text2:
            isSame = False
            break
print(isSame)

print("---------------")
list01 = "Morgen", "Banana", "Apple"
list02 = "Morgen", "Banana", "Apple"

if len(text1) != len(text2):
    isSame = False
else:
    for i in range(len(list01)):
        if list01[i] != list02[i]:
            isSame = False
            break
print(isSame)


print("---------------")

numbers0 = "1 2 3 4 5 0".split()
numbers_name0 = "one two three four five".split()

result0 = zip(numbers0, numbers_name0)
#print(list(result0))
#print(dict(result0))
print(tuple(result0))