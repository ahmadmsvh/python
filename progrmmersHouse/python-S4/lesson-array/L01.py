from array import array
import random

arr = array("i",[0] * 5)

for i in range(0,5):
    arr[i] = random.randint(1,10)
    
for i in range(0,5):
    print(arr[i])

num = int(input("enter a number:\t"))

there_is = False
i = 0

while there_is == False and i < 5:
    if arr[i] == num:
        there_is = True
    i = i + 1

if there_is == True:
    print("%d is in the array" %num)
else:
    print("%d is not in the array" %num)

