a = int(input("A:\t"))
b = int(input("B:\t"))
c = int(input("C:\t"))
d = int(input("D:\t"))

pak = 0
sum = 0
sum += a
if sum > 10:
    pak += 1
    sum =0

sum += b
if sum > 10 :
    pak += 1
    sum = 0

sum += c
if sum > 10:
    pak += 1
    sum = 0

sum += d 
if sum > 10:
    pak += 1

print(pak)