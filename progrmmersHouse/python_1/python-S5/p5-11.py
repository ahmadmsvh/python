#---------------------<< Fibonacci >>--------------------
def fibonacci(num):
 
    if num == 1 or num == 2:
        return 1
    else:
        fibnum = fibonacci(num-1)+fibonacci(num-2)
        
        return fibnum
    
#---------------------<< Fibonacci >>--------------------
def isFibo(num):
    i = 1
    fibonacci(i)
    
    while num > fibonacci(i):
        i += 1
    
    if fibonacci(i) == num:
        print("%d is a fibonacci" % num)
        return True
    else:
        print("%d is not a fibonacci" % num)
        return False
#---------------------<< Main Program >>--------------------
num = int(input("enter a number:\t"))

is_fib = isFibo(num)

    