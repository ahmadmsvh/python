################# make a  matrix #################
def makeArray(row_size,col_size):
    my_matrix = [[0 for x in range(col_size)] for x in range(row_size)]
    input_list = getList()
    for row in range(row_size):
        for col in range(col_size):
            my_matrix[row][col] = int(input_list[0])
            input_list.pop(0)
    return my_matrix
    
################# get a list #################
def getList():
    try:
        str = input('enter elements separated by comma:\n')
        str = str.strip()
        separator = findSeparator(str)
        if separator == "wrong format":
            print(separator)
            raise Exception
        str = str.split(separator)
        return str

    except Exception:
        str = getList()
        return str
        
################# find string separator #################
def findSeparator(str):
    for separator in [' ',' ',',']:
        if str.find(separator) != -1:
            return separator
        
    return "wrong format"

################# get an integer #################
def getInteger():
    try:
        inp = int(input())
        return inp
    except Exception:
        return getInteger()

################# Find saddle point #################
def findSaddlePoint(my_matrix):
    saddle_point_list = []
    for row in my_matrix:
        row_max_index = row.index(max(row))

        col_max = findCol(my_matrix,row_max_index)
        
        col_max_index = col_max.index(max(col_max))
        
        if col_max_index == my_matrix.index(row):
            saddle_point_list.append([my_matrix.index(row) , row_max_index])

    return saddle_point_list

################# find column list #################
def findCol(my_matrix,col_index):
    col_list = []
    for row in my_matrix:
        col_list.append(row[col_index])
    # print(col_list)
    return col_list

################# Main Program #################

print('enter row size:')
row_size = getInteger()
print('enter column size:')
col_size = getInteger()

my_matrix = makeArray(row_size,col_size)

saddle_point_list = findSaddlePoint(my_matrix)
print(saddle_point_list)


