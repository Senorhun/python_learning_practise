file_output = open("file_handling/modified_excel.txt","wt")
file_input = open("file_handling/excel.txt","rt")
output = []
for line in file_input.readlines():
    for element in line:
        output.append(element*2)
file_output.writelines(output)
file_output.close()
