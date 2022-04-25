n = int(input("enter dimention of matrix:\t"))
matrix =[]
for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append((i+1)*(j+1))

for i in range(n):
    row_sum = 0
    for j in range(n):
        row_sum += matrix[i][j]
    matrix[i].append(row_sum)
    
n_plus_row = []
for i in range(n):
    column_sum = 0
    for j in range(n):
        column_sum += matrix[j][i]
    n_plus_row.append(column_sum)
    
matrix.append(n_plus_row)

for x in matrix:
    for y in x :
        print(y,end = "\t")
    print()

print(matrix)