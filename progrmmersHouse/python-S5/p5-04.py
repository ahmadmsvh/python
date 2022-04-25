#---------------------< Prime Number Detector >--------------------

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

#---------------------< Main Program >--------------------

num = int(input("enter a number:\t"))

result = isPrime(num)

print("%d is a prime number: %s " %(num , result))




