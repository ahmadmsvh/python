import random

point=0
counter=0

#---------------------------------------Question 1
r1=random.randint(1,9)
r2=random.randint(1,9)

mult_result=r1*r2

response=int(input("solve this equation %dx%d="%(r1,r2)))

if response==mult_result:
    counter=counter+1

#---------------------------------------Question 2
r1=random.randint(1,9)
r2=random.randint(1,9)

mult_result=r1*r2

response=int(input("solve this equation %dx%d="%(r1,r2)))

if response==mult_result:
    counter=counter+1

#---------------------------------------Question 3
r1=random.randint(1,9)
r2=random.randint(1,9)

mult_result=r1*r2

response=int(input("solve this equation %dx%d="%(r1,r2)))

if response==mult_result:
    counter=counter+1

#---------------------------------------Question 4
r1=random.randint(1,9)
r2=random.randint(1,9)

mult_result=r1*r2

response=int(input("solve this equation %dx%d="%(r1,r2)))

if response==mult_result:
    counter=counter+1

#---------------------------------------Question 5
r1=random.randint(1,9)
r2=random.randint(1,9)

mult_result=r1*r2

response=int(input("solve this equation %dx%d="%(r1,r2)))

if response==mult_result:
    counter=counter+1

point=counter*20

print("you answered %d true out of five question\n your point is %d"%(counter,point))












