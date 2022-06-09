n = int(input("enter n:\t"))
sum = 0
j=-1

for i in range(1,n+1):
    j = -j
    sum = sum + i*j
print("sumation :\t%d" %sum)