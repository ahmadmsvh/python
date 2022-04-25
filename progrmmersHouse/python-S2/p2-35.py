from types import MappingProxyType


num1 = int(input("enter the first number:\t"))
num2 = int(input("enter the second number:\t"))
num3 = int(input("enter the third number:\t"))

max = num1
min = num1
max_position = 1
min_position = 1

if num2 > max :
    max = num2
    max_position = 2
elif num2 < min :
    min = num2
    min_position = 2 

if num3 > max :
    max = num3
    max_position = 3
elif num2 < min :
    min = num3
    min_position = 3

if min_position < max_position: 
    print("right right right")
else: 
    print("no no no")