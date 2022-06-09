num1 = int(input("enter the first number:\t"))
num2 = int(input("enter the second number:\t"))
num3 = int(input("enter the third number:\t"))
num4 = int(input("enter the forth number:\t"))

is_seen_even = False
min = 10

if num1 % 2 == 0 :
    if is_seen_even == False:
       min = num1
       is_seen_even = True
    else:
        if num1 < min :
            min = num1

if num2 % 2 == 0 :
    if is_seen_even == False:
       min = num2
       is_seen_even = True
    else:
        if num2 < min :
            min = num2

if num3 % 2 == 0 :
    if is_seen_even == False:
       min = num3
       is_seen_even = True
    else:
        if num3 < min :
            min = num3

if num4 % 2 == 0 :
    if is_seen_even == False:
       min = num4
       is_seen_even = True
    else:
        if num4 < min :
            min = num4

if is_seen_even == True:   
    print(min)
else:
    print("no even number")