#---------------------<< Factorial >>--------------------
def factorial(num):
    
    result = 1
    
    for i in range(2 , num + 1):
        result *= i
        
    return result

#---------------------<< Prime Number Detector >>--------------------
def fivePower(num):
    
    result = 5 ** num

    return result

#---------------------<< Controller >>--------------------
def fact_pow_controller():
    num = 1
    fact = factorial(num)
    pow = fivePower(num)
    while fact < pow:
        num += 1
        fact = factorial(num)
        pow = fivePower(num)
    return num
#---------------------<< Main Program >>--------------------
number = fact_pow_controller()
print(number)