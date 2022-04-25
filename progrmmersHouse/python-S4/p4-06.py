from array import array

#--------------------------<< make an array >>--------------------------
def makeArray(index):
    input_arr = array("i", [0] * index)
    return input_arr

#--------------------------<< manually fill an array >>--------------------------
def manInitArray(array_name):
    for i in range(0,len(array_name)):
        array_name[i] = int(input("enter an input:"))
    return array_name

#--------------------------<< Main Program>>--------------------------

final = makeArray(20)
temp = makeArray(10)
manInitArray(temp)

for i in range(0,20):
    if i < 10:
        final[i] = temp[9 - i]
    else:
        final[i] = temp[i - 10]
print(final)



# num_array =[]

# for i in range(0,20):
#     if i < 10 :
#         num_array.append(int(input("enter a number:\t")))
#         if i == 9 :
#             num_array.reverse()
#     else:
#         num_array.append(num_array[19-i])
# print(num_array)