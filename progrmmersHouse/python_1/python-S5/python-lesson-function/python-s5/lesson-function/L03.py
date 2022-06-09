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
    
    return result

#--------------------<< Print Line>>--------------------
def print_line():
    for i in range(1,20):
        print("*", end ="")
        
    print("")

#--------------------<< Main Program >>--------------------

res = power()

response = res + 45

print(response)

print_line()