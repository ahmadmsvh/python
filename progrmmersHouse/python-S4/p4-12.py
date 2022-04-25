m = int(input("enter number of members of A:\t"))
A = []
for i in range(0,m):
    A.append(int(input("enter members of A:\t")))
AA = A.copy()
n = int(input("enter number of members of B:\t"))
B = []
for i in range(0,n):
    B.append(int(input("enter members of B:\t")))
BB = B.copy()
j = 0
k = 0
C = []
for i in range(0,m+n):
    if  j < n and i % 3 == 2 :
        C.append(B[0])
        B.pop(0)
        j += 1
    elif k < m :   
        C.append(A[0])
        A.pop(0)
        k += 1
    elif k >= m and j < n :
        C.append(B[0])
        B.pop(0)
        j += 1

print(AA)
print(BB)    
print(C)    

# m = int(input("enter number of members of A:\t"))
# A = []
# for i in range(0,m):
#     A.append(int(input("enter members of A:\t")))
    
# n = int(input("enter number of members of B:\t"))
# B = []
# for i in range(0,n):
#     B.append(int(input("enter members of B:\t")))

# j = 0
# k = 0
# C = []
# for i in range(0,m+n):
#     if (i % 3) == 2 and k < n:
#         C.append(B[k])
#         k += 1 
#     else:
#         if j < m:
#             C.append(A[j])
#             j += 1 
#     if k >= n and j <m:
#         C.append(A[j])
#         j += 1   
#     elif j >= m and k < n:
#         C.append(B[k])
#         k += 1 

# print(A)
# print(B)    
# print(C)    