print("---------slice--------")

tupleVektor = (0, 1, 2, 3, "c", 4, 5, 6, 7, 8, 9)

tupleVektor1 = tupleVektor[:4] + tupleVektor[5:]

print(tupleVektor)
print(tupleVektor1)

print("---------convert--------")

listTuple = list(tupleVektor)
print(listTuple)
listTuple.remove("c")  # listTuple.pop(4)

print(listTuple)
