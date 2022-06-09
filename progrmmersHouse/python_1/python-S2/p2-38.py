num1 = int(input("enter the first number:\t"))
num2 = int(input("enter the second number:\t"))
num3 = int(input("enter the third number:\t"))
num4 = int(input("enter the forth number:\t"))

counter=0

if num1 % 2 == 0 :
    counter += 1
    if counter == 1 :
        min_even = num1
    if num1 < min_even:
        min_even = num1

if num2 % 2 == 0 :
    counter += 1
    if counter == 1 :
        min_even = num2
    if num2 < min_even:
        min_even = num2

if num3 % 2 == 0 :
    counter += 1
    if counter == 1 :
        min_even = num3
    if num3 < min_even:
        min_even = num3

if num4 % 2 == 0 :
    counter += 1
    if counter == 1 :
        min_even = num4
    if num4 < min_even:
        min_even = num4

if counter > 0:
    print("minimum even number is %d"%min_even)
else:
    print("there is no even number")
