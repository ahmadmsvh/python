#---------------------< Count 3 Multiples >--------------------

def mult3Count(num):
    
    counter = 0
    
    for i in range(3,num,3):
        counter += 1
        
    return counter

#---------------------< Main Program >--------------------

num = int(input("enter a number:\t"))

mult3 = mult3Count(num)

print(mult3)




