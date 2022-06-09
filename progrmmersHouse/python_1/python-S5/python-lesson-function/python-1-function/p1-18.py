#-------------------------<< Add >>-------------------------
def addTwoNumber(num1 , num2):
    sum = num1 + num2
    print("%d + %d = %d" %(num1,num2,sum))
    
    return sum
#-------------------------<< Subtract >>-------------------------
def subtractTwoNumber(num1 , num2):
    sub = num1 - num2
    print("%d - %d = %d" %(num1,num2,sub))
    
    return sub
#-------------------------<< Multi >>-------------------------
def multiplyTwoNumber(num1 , num2):
    multi = num1 * num2
    print("%d * %d = %d" %(num1,num2,multi))
    
    return multi
#-------------------------<< Devide >>-------------------------
def divideTwoNumber(num1 , num2):
    divd = num1 / num2
    print("%d / %d = %d" %(num1,num2,divd))
    
    return divd
#-------------------------<< Get Number >>-------------------------
def enterNumber():
    num = int(input("Please enter a number:\t"))
    
    return num
#-------------------------<< Main Program >>-------------------------
num1 = enterNumber()
num2 = enterNumber()

add = addTwoNumber(num1,num2)
sub = subtractTwoNumber(num1,num2)
mult = multiplyTwoNumber(num1,num2)
div= divideTwoNumber(num1,num2)


