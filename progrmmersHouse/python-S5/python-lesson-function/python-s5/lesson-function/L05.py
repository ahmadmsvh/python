#--------------------<< Prime Number Detector >>--------------------
def is_prime_number(number):
    is_seen_prime = True
    i = 2
    while is_seen_prime == True and i <= number // 2:
        if number % i == 0:
            is_seen_prime = False
        i = i + 1 
    if is_seen_prime == True and number != 0 and number != 1:
        return True
    else:
        return False
        
#--------------------<< Power Calculator >>--------------------
def power(num1,num2):
    result = 1
    pow = num2

    if pow < 0:
        num2 = num2 *(-1)
    
    for i in range(1,num2 + 1):
        result = result * num1
        
    if pow < 0:
        result = 1 / result
    return result
    
#--------------------<< Main Program >>--------------------
n = 11

is_seen_prime = is_prime_number(n)

n1 = 2
n2 = 3

res  = power(n1,n2)

if is_seen_prime == True:
    print(res + n)
else:
    print(res)

