num1 = int(input("enter the first number:\t"))
num2 = int(input("enter the second number:\t"))
num3 = int(input("enter the third number:\t"))
num4 = int(input("enter the forth number:\t"))
num5 = int(input("enter the fifth number:\t"))
num6 = int(input("enter the fifth number:\t"))
num7 = int(input("enter the fifth number:\t"))
num8 = int(input("enter the fifth number:\t"))
num9 = int(input("enter the fifth number:\t"))
num10 = int(input("enter the fifth number:\t"))

even_counter = 0
even_counter_max = 0

if num1 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

if num2 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

if num3 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

if num4 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

if num5 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

if num6 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

if num7 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

if num8 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

if num9 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

if num10 % 2 == 0:
    even_counter += 1
else:
    if even_counter > even_counter_max:
        even_counter_max = even_counter
    
    even_counter = 0

print("maximum enen number in a row:\t%d"%even_counter_max)