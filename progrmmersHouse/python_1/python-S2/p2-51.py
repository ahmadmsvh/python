a = int(input("A:\t"))
b = int(input("B:\t"))
c = int(input("C:\t"))
d = int(input("D:\t"))

temp = a
a = b
b = d
d = c

if b > temp :
    c = temp
else:
    c = b
    b = temp

print("\nA:\t%d\nB:\t%d\nC:\t%d\nD:\t%d\n"%(a,b,c,d))