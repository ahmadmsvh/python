num1 = int(input("enter the fist number:\t"))
num2 = int(input("enter the power number:\t"))
i = 0
result = 1

while i < num2:
    result *= num1
    i += 1
print("%d ^ %d = %d" %(num1,num2,result))