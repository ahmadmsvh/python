#--------------------<< Say Hello World >>--------------------
def say_hello_world():
    print("hello world!")
    print("I love life")
    print("Hardships make a person stronger")
    print("When the going gets tough, the tough get going")
    print("hello world!")
    print("atmetif ein. es ist nur eine schwere zeit,kein schweres leben")
    print("BETTER DAYS ARE COMING")
    print("you can`t do it all at once but you can do it al")
    print("without hustle talent will only carry you so far")
    print("BE A VOICE NOT AN ECHO")
    
#--------------------<< Draw Triangle >>--------------------
def draw_triangle():
    for i in range(1,6):
        for j in range(1,i+1):
            print("*", end = "")
        print("")  
    
#--------------------<< Prime Number Detector >>--------------------
def is_prime_number():
    number = int(input("enter a number to recognise it is prime or not:\t"))
    is_seen_prime = True
    i = 2
    while is_seen_prime == True and i <= number // 2:
        if number % i == 0:
            is_seen_prime = False
        i = i + 1 
    if is_seen_prime == True and number != 0 and number != 1:
        print("%d is a prime number" %number)
    else:
        print("%d is not prime" %number)
        
#--------------------<< Print Line>>--------------------
def print_line():
    for i in range(1,20):
        print("*", end ="")
    print("")

#--------------------<< Power Calculator >>--------------------
def power():
    num1 = int(input("enter a nummber:\t"))
    num2 = int(input("enter the power:\t"))
    result = 1
    pow = num2

    if pow < 0:
        num2 = num2 *(-1)
    
    for i in range(1,num2 + 1):
        result = result * num1
        
    if pow < 0:
        result = 1 / result
    print(result)

#--------------------<< Main Program >>--------------------
say_hello_world()

draw_triangle()

is_prime_number()

draw_triangle()

say_hello_world()

print_line()

power()
