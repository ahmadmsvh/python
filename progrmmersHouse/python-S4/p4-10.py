num1 = str(input("enter a binary number:\t"))
num2 = str(input("enter a binary number:\t"))
num1_int = 0
num2_int = 0
    
for i in range(0,len(num1)):
    num1_int = num1_int * 2 + int(num1[i])

for i in range(0,len(num2)):
    num2_int = num2_int * 2 + int(num2[i])
    
# print(bin(num1_int + num2_int))
sum = num1_int + num2_int
quotion = sum
binary_array = []

while quotion > 0 :
    rem = quotion % 2
    quotion //= 2
    binary_array.append(str(rem))

binary_array.reverse()
binary_sum = ""

for i in range(0,len(binary_array)):
    binary_sum += binary_array[i]
    
print(binary_sum)
