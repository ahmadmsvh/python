from array import array
import random

#--------------------------<< make an array >>--------------------------
def makeArray(index):
    input_arr = array("i", [0] * index)
    return input_arr

#--------------------------<< randomly fill an array >>--------------------------
def generateRandom(array_name,iterration):
    for i in range(0 , iterration):
        rand = random.randint(1,6)
        array_name[rand] = array_name[rand] + 1
    return array_name

#--------------<< randomly fill an array >>--------------
def calcIterration(array_name):
    for i in range(1,7):
        print(" %d has happend %d times. " %(i,array_name[i]))
        
#--------------------------<< Main Program >>--------------------------
dice_array = makeArray(7)

result = generateRandom(dice_array,200)

calcIterration(result)
