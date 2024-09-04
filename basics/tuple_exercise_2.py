listStarter = [87, 45, 41, 65, 94, 41, 99, 94]
print("-------for--------")

print(f"Original list: {listStarter}")

resultList = []
numToTrash = []
for num in listStarter:
    if listStarter.count(num) == 1 or num not in resultList:
        resultList.append(num)
    else:
        numToTrash.append(num)
resultTuple = tuple(resultList)
print(f"Result list: {resultTuple}")
print(f"Duplicants: {numToTrash}")

print("-------set--------")
listSet = list(set(listStarter))
listTupleSet = tuple(listSet)
print(f"Original list: {listStarter}")
print(f"Result list: {resultTuple}")
print(f"Lowest element: {min(listTupleSet)}")
print(f"highest element: {max(listTupleSet)}")