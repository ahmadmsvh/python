from array import array

#--------------------------<< make an array >>--------------------------
def makeArray(index):
    input_arr = array("i", [0] * index)
    return input_arr

#--------------------------<< filling an array >>--------------------------
def arrFill(arrName):
    for x in range(0,len(arrName)):
        arrName[x] = int(input("enter array data:\t"))
    return arrName 

#--------------------------<< copy array >>--------------------------
def copyArray(arrName,arrNameCopy):
    for i in range(0,len(arrName)):
        arrNameCopy[len(arrName)-1 - i] = arrName[i]
    return arrNameCopy

#--------------------------<< Main Program >>--------------------------
arr1 = makeArray(5)
arrFill(arr1)

arr2 = makeArray(5)

copyArray(arr1 , arr2)

print(arr1 , arr2)





# my_array = ["ali","emad","saam"]

# new_array = my_array.copy()
# new_array.reverse()

# print(my_array)
# print(new_array)