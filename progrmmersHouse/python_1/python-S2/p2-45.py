a = int(input("A:\t"))
b = int(input("B:\t"))
c = int(input("C:\t"))
d = int(input("D:\t"))

a_remainder = a % 3
b_remainder = b % 3
c_remainder = c % 3
d_remainder = d % 3

if a_remainder == b_remainder:
    print("a:%d  b:%d"%(a,b))

elif b_remainder == c_remainder:
    print("b:%d  c:%d"%(b,c))

elif c_remainder == d_remainder:
    print("c:%d  d:%d"%(c,d))