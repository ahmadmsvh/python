print("enter 2 numbers to check if they are devidable by 3 or 7")
num1=int(input("enter the first number: \t"))
num2=int(input("enter the second number:\t"))

if (num1%3==0 and num2%3==0)  :
    print("message:yes\t1")
elif (num1%7==0 and num2%7==0):
    print("message:yes\t1")
else:
    print("message:no\t2")
