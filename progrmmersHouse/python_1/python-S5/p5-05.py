#---------------------<< Prime Number Detector >>--------------------
def isPrime(num):
    
    if num <= 1:
        return False
        
    is_prime = True
    i = 2
    
    while is_prime == True and i <= num // 2:
        if num % i == 0 :
            return False
        i += 1
    return True

        
#---------------------<< Printing >>--------------------
def printPrime(is_prime , prime):
    if is_prime == True:
        print(prime)
        
#---------------------<< Number Generator >>--------------------
def rangeNumber():
    for i in range(1 , 101):
        is_prime = isPrime(i)
        printPrime(is_prime , i)

#---------------------<< Main Program >>--------------------

rangeNumber()