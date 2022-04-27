import random

def makeArray(row,col):
    rand_array = [[random.randint(0,100) for x in range(col)] for x in range(row)]
    return rand_array

def streamArray(my_array):
    stream = []
    for row in my_array:
        for col in row:
            stream.append(col)
    return stream

def sortArray(my_array):
    row_size = len(my_array)
    col_size = len(my_array[0])

    stream = streamArray(rand_array)
    stream.sort()

    for row in range(row_size):
        for col in range(col_size):
            my_array[row][col] = stream[0]
            stream.pop(0)
    return my_array

########### Main Program ###########

row = int(input('enter row:\t'))
col = int(input('enter col:\t'))
print()

rand_array = makeArray(row,col)
for x in rand_array:
    print(x)

print()

rand_array_sort = sortArray(rand_array)

for x in rand_array_sort:
    print(x)



