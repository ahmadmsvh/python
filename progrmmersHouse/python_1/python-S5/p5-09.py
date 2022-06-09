#---------------------< Prime Number >--------------------
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

#---------------------<< Finde Band Primes >>--------------------
def countPrime(num):
    counter = 0
    
    for i in range(num , num + 99):
        is_prime = isPrime(i)
        
        if is_prime == True:
            counter += 1
            
    return counter

#---------------------<< Finde Band >>--------------------
def findMostPrimeRange(n , m):
    max = 0 
    
    for i in range (n , m , 100):
        number_of_primes = countPrime(i)
        
        if number_of_primes > max:
            max = number_of_primes
            max_band = i
            
    return max_band

#---------------------<< Main Program >>--------------------
max_band = findMostPrimeRange(1 , 10000)

print(max_band , max_band + 99)