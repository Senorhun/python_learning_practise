list = [25, 69, 54, 8, 77, 6, 29, 10, 3, 98]

result = "The list: "
for number in list:
    result += " " + str(number)

print(result)

result = "The indexed list: "
smallestNumber = list[0]
smallestNumberIndex = None
for index, number in enumerate(list):
    if number < smallestNumber:
        smallestNumber = number
        smallestNumberIndex = index
    result += f" [{index}]={number}"


print(result)
print(f"Result smallest number is: [{smallestNumberIndex}]={smallestNumber}")

print()
result2 = "The list: "
for number in list:
    if number == smallestNumber:
        result2 += f" {smallestNumber}[MIN]"
    else:
        result2 += f" {number}"

print(result2)

print("-----")
result3 = []
for n in list:
    result3.append(f"{n}{"[MIN]" if n == smallestNumber else ""}")
print(result3)