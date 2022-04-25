number_1=int(input("enter the first number:\t"))
number_2=int(input("enter the second number:\t"))

if (100 > number_1 > 9 and 100 > number_2 > 9):
    a = number_1 % 10
    b = number_1 // 10
    c = number_2 % 10
    d = number_2 // 10
    if a==c or a==d :
        print("there are some similar digits in this two numbers")
    elif b==c or b==d :
       print("there are some similar digits in this two numbers")
    else:
        print("there is no similar digit here")
else:
    print("out of range")