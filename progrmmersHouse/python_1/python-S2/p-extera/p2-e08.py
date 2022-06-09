number_one=float(input("enter the first number:\t"))
number_two=float(input("enter the second number:\t"))
number_three=float(input("enter the third number:\t"))
number_four=float(input("enter the forth number:\t"))
number_five=float(input("enter the fifth number:\t"))

maximum=number_one
minimum=number_one
average=(number_one+number_two+number_three+number_four+number_five)/5

if number_two>maximum:
    maximum=number_two
elif number_two<minimum:
    minimum=number_two

if number_three>maximum:
    maximum=number_three
elif number_three<minimum:
    minimum=number_three   

if number_four>maximum:
    maximum=number_four
elif number_four<minimum:
    minimum=number_four  
             
if number_five>maximum:
    maximum=number_five
elif number_five<minimum:
    minimum=number_five  

print("the maximum number is '%f' and the minimum number is '%f'and the average is '%f'"%(maximum,minimum,average))         

