list = [-25, 12, -54, 8, 77, 98, -29, 35, 3, 71]

list.sort()
print(list[len(list) - 1])

print("-------------------------")
biggestNumber = list[0]
for number in list:
    print(f"We compare  {number} to {biggestNumber}")
    if number > biggestNumber:
        biggestNumber = number
    print(f"Recent biggest number is {biggestNumber}")

print(f"---> The result number is {biggestNumber}")
