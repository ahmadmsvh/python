def makeArray(row,col):
    my_array = []
    for i in range(row):
        row_input = getInput(col)
        my_array.append(row_input)
    
    return my_array


def getInput(col):
    try:
        inp = input("enter first row %d elements seprated by comma:\t"%col)
        inp = inp.strip()
        separator = findSeparator(inp)

        if separator == 'wrong format':
            raise Exception
        inp = inp.split(separator)
        if len(inp) != col:
            raise Exception
        return inp

    except Exception:
        print('wrong format! enter row again:')
        inp = getInput(col)
        return inp


def findSeparator(str):
    for separator in [' ',',','.']:
        if str.find(separator) != -1:
            return separator
    else:
        return 'wrong format'

def getInteger():
    try:
        inp = int(input())
        return inp
    except Exception:
        inp = getInteger
        return inp

def makeDiff(my_array):
    out_array = [[0 for i in range(len(my_array[0]) * 2)] for i in range(len(my_array))]
    
    row_size = len(my_array)
    col_size = len(my_array[0])

    for row in range(row_size):
        for col in range(col_size):
            out_array[row][col_size -1 - row + col] = my_array[row][col]
    return out_array

#---------------------Main Program#---------------------

print('enter number of rows')
row = getInteger()
print('enter number of columns')
col = getInteger()

first_array = makeArray(row,col)
second_array = makeDiff(first_array)

for x in second_array:
    print(x)
