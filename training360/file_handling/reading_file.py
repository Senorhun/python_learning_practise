
file_input = open("file_handling/excel.txt", "rt")
goods = []
for line in file_input.readlines()[1:]:
    goodsLine = line.split("|")
    goods.append(goodsLine)
file_input.close()
print(goods)


#simply read from file
#file_input = open("file_handling/excel.txt", "r")
#print(file_input.read())