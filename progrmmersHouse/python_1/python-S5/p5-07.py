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

#---------------------<< Next Prime Number Detector >>--------------------

def findNextPrime(num):
    
    is_prime = False
    
    while is_prime == False:
        num = num + 1
        
        is_prime = isPrime(num)
        
        if is_prime == True:
            return num

#---------------------< Main Program >--------------------
num = int(input("enter a number:\t"))

prime_number = findNextPrime(num)

print("the first prime number greater than %d is %d" %(num , prime_number))