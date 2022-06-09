#---------------------< Summation >--------------------

def print_numbers(inp_num):
    
    sum = 0
    
    for i in range(1,inp_num + 1):
        sum += i
        
    return sum

#---------------------< Main Program >--------------------

num = int(input("enter a number:\t"))

summation = print_numbers(num)

print(summation)




