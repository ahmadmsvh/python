a = int(input("A:\t"))
b = int(input("B:\t"))
c = int(input("C:\t"))

if a > b:
    difab = a - b
else:
    difab = b - a
    
if a > c:
    difac = a - c
else:
    difac = c - a

if b > c:
    difbc = b - c
else:
    difbc = c - b

min = difab

if difac < min:
    min = difac

if difbc < min:
    min = difbc

print("minimum distance is %d" %min)