from array import array

#--------------------------< Mmaking Array >--------------------------
def makeArray(number):
    the_array = array("i", [0] * number)
    return the_array

#--------------------------< Main Program >--------------------------
def manualFillArray(array_name):
    for i in range(0,len(array_name)):
        number = int(input("enter a number:\t"))
        array_name[i] = number
        
#--------------------------< Most Repeated >--------------------------
def findMostRepeated(array_name):
    max_repeat = 0
    for  i in range(0,len(array_name)):
        counter = array_name.count(array_name[i])
        
        if counter > max_repeat:
            max_repeat = counter
            max_repeat_element = array_name[i]
            
    return max_repeat,max_repeat_element

#--------------------------< Main Program >--------------------------
numbers = makeArray(20)

manualFillArray(numbers)

most_repeat = findMostRepeated(numbers)

print("%d, has beed repeated in the array %d times" %(most_repeat[1],most_repeat[0]))