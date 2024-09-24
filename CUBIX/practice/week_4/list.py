matrix1 = [[i*j for i in range(3)] for j in range(4)]
matrix2 = matrix1.copy()
print(matrix1)
matrix1[0][0] = 10
print(matrix1)
print(matrix1[0][0])