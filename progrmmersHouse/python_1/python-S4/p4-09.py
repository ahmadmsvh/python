from array import array

#--------------------------<< make an array >>--------------------------
def makeArray(index):
    input_arr = array("i", [0] * index)
    return input_arr

#--------------------------<< Make an Hex >>--------------------------
def convertToHex(number):
    hex = makeArray(0)
    
    while number // 16 > 0:
        rem = number % 16
        number = (number - rem) / 16
        if rem == 10 :
            rem = "a"
        elif rem == 11:
            rem = "b"
        elif rem == 12:
            rem = "c"   
        elif rem == 13:
            rem = "d"
        elif rem == 14:
            rem = "e" 
        elif rem == 15:
            rem = "f"
            
        hex.insert(1,rem)

    return hex
#--------------------------<< Main Program >>--------------------------
number = int(input("enter a number to convert to hexadecimal: \t"))
hex = convertToHex(number)
print(hex)


# decimal_number = int(input("enter a number:\t"))
# q = decimal_number
# hexa_decimal = ""
# hex_array = []
# i = 0
# while q > 0 :
#     rem = q % 16
#     q //= 16
#     if rem == 10 :
#         rem = "A"
#     if rem == 11 :
#         rem = "B"
#     if rem == 12 :
#         rem = "C"
#     if rem == 13 :
#         rem = "D"
#     if rem == 14 :
#         rem = "E"
#     if rem == 15 :
#         rem = "F"
#     hex_array.append(str(rem))
    
# hex_array.reverse()

# for i in range(0,len(hex_array)):
#     hexa_decimal += hex_array[i]
    
# print(hexa_decimal)
        
    

