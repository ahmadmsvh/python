num1=int(input("enter first number:\t"))
num2=int(input("enter second number:\t"))
num3=int(input("enter third number:\t"))

counter_two=0
counter_three=0

if num1%2==0:
    counter_two+=1
if num2%2==0:
    counter_two+=1
if num3%2==0:
    counter_two+=1

if num1%3==0:
    counter_three+=1
if num2%3==0:
    counter_three+=1
if num3%3==0:
    counter_three+=1

if counter_two>counter_three:
    print("%d of three entered number is devidable by '2' "%counter_two)
elif counter_three>counter_two:
     print("%d of three entered number is devidable by '3' "%counter_three)
else:
    print("none")