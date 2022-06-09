num1 = int(input("enter the first number:\t"))
num2 = int(input("enter the second number:\t"))

if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

num1 = num1 + (7 - (num1 % 7))

counter = 0

for i in range(num1,num2,7):
    counter += 1

print(counter)
