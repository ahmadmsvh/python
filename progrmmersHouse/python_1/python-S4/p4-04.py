from array import array

def buildArray(length):
    array_name = array("i", [0] * length)
    return array_name

def fillArray(array_name):
    for i in range(len(array_name)):
        array_name[i] = int(input("enter a number:\t"))
    return array_name

#-------------<< summation of ones of array elements >>-------------
def sumArryOnes(array_name):
    sum = 0 
    for i in range(len(array_name)):
        rem = array_name[i] % 10
        sum = sum + rem
    return sum

#-------------<< find an element in an array >>-------------
def findElement(array_name,element):
    for i in range(len(array_name)):
        if array_name[i] == element:
            return i
    i = -1
    return i

#-------------<< Main Program >>-------------
my_array = buildArray(15)
my_array = fillArray(my_array)

sum = sumArryOnes(my_array)

index_of_element = findElement(my_array,sum)

if index_of_element != -1:
    print(my_array[index_of_element])
else: 
    print("there is no match")


# from array import array

# #--------------------------<< make an array >>--------------------------
# def makeArray(index):
#     input_arr = array("i", [0] * index)
#     return input_arr

# #--------------------------<< manually fill an array >>--------------------------
# def manInitArray(array_name):
#     for i in range(0,len(array_name)):
#         array_name[i] = int(input("enter an input:"))
#     return array_name

# #--------------------------<< find in array >>--------------------------

# def isInArray(array_name,element):
#     for i in range(0,len(array_name)):
#         if array_name[i] == element:
#             return True
#     return False
            

# #--------------------------<< Main Program >>--------------------------
# first_array = makeArray(15)

# manInitArray(first_array)

# sum = 0 

# for i in range(0,len(first_array)):
#     sum += first_array[i] % 10 

# print(isInArray(first_array,sum))






# num_array = []
# for i in range (0,15):
#     num_array.append(int(input("enter a number:\t")))

# for i in range(0,15):
#     sum_ones = 0
#     for j in range(0,15):
#         if num_array[i] != num_array[j] :
#             sum_ones += num_array[j] % 10
#     if num_array[i] == sum_ones :
#         print (num_array[i], sum_ones,"\tyes")
#     else:
#         print(num_array[i],sum_ones)
            
