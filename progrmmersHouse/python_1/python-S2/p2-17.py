num1=int(input("enter first number:\t"))
num2=int(input("enter second number:\t"))
num3=int(input("enter third number:\t"))
num4=int(input("enter forth number:\t"))

counter_three=0

if num1%3==0:
    counter_three+=1
    
if num2%3==0:
    counter_three+=1

if num3%3==0:
    counter_three+=1

if num4%3==0:
    counter_three+=1


if counter_three%2==0:
    print("%d (even) of four entered number is devidable by '3' "%counter_three)
