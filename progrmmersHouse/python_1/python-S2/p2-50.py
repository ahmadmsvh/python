a = int(input("A:\t"))
b = int(input("B:\t"))
c = int(input("C:\t"))

aa = a % 3

if aa != 0:
    if aa == 1:
        print("b:%d"%b)
    else:
        print("c:%d"%c)