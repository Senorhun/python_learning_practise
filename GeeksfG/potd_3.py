# input_list = [9,4,-2,-1,5,0,-5,-3,2]
input_list = [-1,0,6,-4,2,7,5,-9,3]

positive_numbers = [pos for pos in input_list if pos >= 0]
negative_numbers = [neg for neg in input_list if neg < 0]
print(positive_numbers)
print(negative_numbers)

length = min(len(positive_numbers),len(negative_numbers))
result = []
for i in range(length):
    result.append(positive_numbers[i])
    result.append(negative_numbers[i])

result.extend(positive_numbers[length:])
result.extend(negative_numbers[length:])

print(result)