#-------------------------<< Add Two Number >>-------------------------
def addTwoNumber(num1 , num2):
    sum = num1 + num2
    return sum
#-------------------------<< Get Number >>-------------------------
def enterNumber():
    num = int(input("enter a number:\t"))
    return num
#-------------------------<< Main Program >>-------------------------
number_one = enterNumber()
number_two = enterNumber()
sum = addTwoNumber(number_one , number_two)
print(sum)