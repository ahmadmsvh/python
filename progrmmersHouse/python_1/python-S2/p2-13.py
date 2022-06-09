print("enter two numbers to choose the greater one and")
num1=int(input("enter the first number:\t"))
num2=int(input("enter the second number:\t"))

max=num1

if num2>num1:
    max=num2

quotient=max//10
remainder=max%10

print("%d devided by 10 gives %d as quotient and %d as remainder"%(max,quotient,remainder))

