numList = [47,64,69,37,76,83,95,97]
resultList = []
print(numList)
sampleDict = {'Jhon':47, 'Emma':69,'Kelly':76,'Jason':97}

for num in numList:
    if num in sampleDict.values():
        resultList.append(num)
print(resultList)

print("--------the python way------") #epic

pythonList = (num for num in numList if num in sampleDict.values())
print(list(pythonList))