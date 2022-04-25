def isPrime(inp):
    i=2
    is_prime = True
    if inp == 2 or inp == 3 :
        return True
    while is_prime == True and i <= inp//2:
        if inp % i == 0:
            is_prime = False
        i += 1   
    
    return is_prime

def findPrimeDivisors(inp):
    result = []
    primecheck = isPrime(inp)
    if primecheck == True:
        result.append(inp)
        return result
    for i in range(2, inp // 2 +1):
        primecheck = isPrime(i)
        if primecheck == True:
            if inp % i == 0:
                result.append(i) 
    
    return result

my_dic = {}
for i in range(10):
    inp = int(input())
    my_dic[inp] = findPrimeDivisors(inp)

# print(my_dic)

max_prime_divisors = 0
the_number = 0

for x,y in my_dic.items():
    if len(y) == max_prime_divisors and x > the_number:
        max_prime_divisors = len(y)
        the_number = x
    if len(y) > max_prime_divisors:
        max_prime_divisors = len(y)
        the_number = x
 
print(the_number,max_prime_divisors)