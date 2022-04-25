#---------------------< Next Prime Number >--------------------

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
#---------------------< Next Prime Number >--------------------

def findNextPrime(num):
    is_prime = False
    
    while is_prime == False:
        num = num + 1
        
        is_prime = isPrime(num)
        
        if is_prime == True:
            return num

#---------------------< nth Prime Number >--------------------

def nthPrimeNumber(num , step):
    next_prime = num
    
    for i in range(step):
        next_prime = findNextPrime(next_prime)
        
    return next_prime
    
#---------------------< Main Program >--------------------
num = int(input("enter a number:\t"))
step = int(input("enter a number:\t"))

number = nthPrimeNumber(num , step)

print("the %dth prime number greater than %d is %d" %(step , num , number))