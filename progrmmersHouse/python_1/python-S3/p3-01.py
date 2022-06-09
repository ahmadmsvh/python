num1 = int(input("enter the first number:\t"))
num2 = int(input("enter the second number:\t"))

if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

for i in range(num1+1,num2):
    num1 +=1
    print(num1)
