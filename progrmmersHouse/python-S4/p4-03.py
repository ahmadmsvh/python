from array import array
import random

#--------------------------<< make an array >>--------------------------
def makeArray(index):
    input_arr = array("i" , [0] * index)
    return input_arr

#--------------------------<< manually fill an array >>--------------------------
def manInitArray(arrayName):
    for i in range(0,len(arrayName)):
        arrayName[i] = int(input("enter an input:"))
    return arrayName

#--------------------------<< randomly fill an array >>--------------------------
def randInitArray(arrayName):
    for i in range(0,len(arrayName)):
        arrayName[i] = random.randint(100,1000)
    return arrayName

#--------------------------<< Main Program>>--------------------------
first_array = makeArray(10)
result_array = makeArray(1)

manInitArray(first_array)

rem23 = False

for i in range(0, len(first_array)):
    for j in range(i+1 , len(first_array)):
        if first_array[i] % 23 == first_array[j] % 23:
            rem23 = True
            print(first_array[i], first_array[j])

if rem23 == True:
    print("yes there is")
else:
    print("no there isn't")





# num_array = []
# for i in range(0,10):
#     num_array.append(int(input("enter a number:\t"))) 

# for i in range(0,10):
#     for j in range(i+1,10):
#         if num_array[i] % 23 == num_array[j] % 23:
#             print("yes")
#             print(num_array[i],num_array[j])