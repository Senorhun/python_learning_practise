for i in range(5):
    print(i)

print("---")
for i in range(1,6,2):
    print(i)

print("---")
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")

print("---")
for fruit in ["apple","banana","coconut"]:
    print(fruit)

print("---")
i = 0
while i < 5:
    print(i)
    i += 1

print("---")
i = 0
while True:
    i += 1
    if i > 20:
        break
    if i == 2:
        continue
    if i % 3 == 0:
        print(str(i) + " odd and div by three")
    else:
        print(i)