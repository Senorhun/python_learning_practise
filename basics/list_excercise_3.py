list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)
list.reverse()
print(list)
print()
print("------algorithmic solution-----")
result = []
for number in range(len(list) - 1, -1, -1):
    result.append(number)

print(result)
print("------algorithmic solution pop-----")
list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"original list2: {list2}")
listNew = []
for number in range(
    len(list2) - 1, -1, -1
):  # for number in range(len(list2), 0, -1): means the same just play with index numbers
    listNew.append(list2.pop())

print(f"listNew: {listNew}")

print("------algorithmic solution switch-----")
list3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(list3) // 2 + 1, 1):
    a = list3[i]
    b = list3[len(list) - 1 - i]
    list3[i] = b
    list3[len(list3) - 1 - i] = a
print(list3)
