print("enter 4 number for considering")
num1=int(input("enter the first number: \t"))
num2=int(input("enter the second number:\t"))
num3=int(input("enter the third number: \t"))
num4=int(input("enter the fifth number: \t"))

if (num1>=num2 and num3>=num4):
    print("entered numbers are in desired format")
elif (num1<=num2 and num3<=num4):
    print("entered numbers are in desired format")
else:
    print("entered numbers are not in desired format")