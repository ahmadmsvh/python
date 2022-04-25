#---------------------<< Fibonacci >>--------------------
def fibonacci(num):
 
    if num == 1 or num == 2:
        return 1
    else:
        fibnum = fibonacci(num-1)+fibonacci(num-2)
        
        return fibnum
    
#---------------------<< Main Program >>--------------------
number = int(input("enter the number of fibonacci series:\t"))

fibo = fibonacci(number)

print(fibo)