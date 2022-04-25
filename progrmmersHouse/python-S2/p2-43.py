a = int(input("A:\t"))
b = int(input("B:\t"))
c = int(input("C:\t"))
d = int(input("D:\t"))

if a != b and a != c and a != d:
    print("the number is a")

if b != a and b != c and b != d:
    print("the number is b")   

if c != b and c != a and c != d:
    print("the number is c")

if d != b and d != c and d != a:
    print("the number is d")