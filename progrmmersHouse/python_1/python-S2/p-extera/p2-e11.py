import random
r=random.randint(1,20)

num=int(input("enter a number between 1 and 20:\t"))

dif=r-num
if dif<0:
    dif=dif*(-1)

point=100-(dif*5)
print("your number is: %d\nrandom number is: %d\nyour point is:%d" %(num,r,point))



