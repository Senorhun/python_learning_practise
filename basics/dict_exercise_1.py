list = [11,45,8,11,23,45,23,45,89]
print(list)
dictList = {}

for num in list:
    if num not in dictList:
     dictList[num] = list.count(num)
print(dictList)

print("-----for-----")
list = [11,45,8,11,23,45,23,45,89]
countDict = dict()

for num in list:
    if num in countDict:
        countDict[num] += 1
    else:
        countDict[num] = 1

print(countDict)

