A=float(input("A:\t"))
B=float(input("B:\t"))
C=float(input("C:\t"))
D=float(input("D:\t"))

shift_memo = 0

if (not(A>B>C)):
    print ("you have problem with entered numbers")

if ((A>B>C)):
    if (D>A):
        shift_memo=D
        D=C
        C=B
        B=A
        A=shift_memo
    elif (D<A and D>B):
        shift_memo=D
        D=C
        C=B
        B=shift_memo
    elif (D<B and D>C):
        shift_memo=D
        D=C
        C=shift_memo
    print("A = %f\nB = %f\nC = %f\nD = %f" %(A,B,C,D))

