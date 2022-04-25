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

#--------------------------<< Print Array >>--------------------------
def printArray(array_name):
    for i in range(len(array_name)-1,-1,-2):
        print(array_name[i])
        
#--------------------------<< Main Program >>--------------------------
numbers = makeArray(7)
numbers = arrFill(numbers)
printArray(numbers)




# my_array = []
# for i in range(0,7):
#     my_array.append(int(input("enter a number:\t")))

# for j in range(0,7):
#     if j % 2 == 1 :
#        print(my_array[j]) 
       
# for j in range(5,0,-2):
#     print(my_array[j])