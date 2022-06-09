A = int(input("A:\t"))
B = int(input("B:\t"))
C = int(input("C:\t"))

if A < B:
    temp = A
    A = B
    B = temp
    
if A < C :
    temp = A
    A = C
    C = temp

if B < C:
    temp = B
    B = C
    C = temp
    
print("\n\nA:\t%d\nB:\t%d\nC:\t%d\n\n"%(A,B,C))