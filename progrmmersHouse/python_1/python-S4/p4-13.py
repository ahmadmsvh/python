A = []
B = []
temp1 = []

n = int(input("enter number of array members:\t"))
for i in range(n):
    A.append(int(input("enter A[%d]:\t" %i)))
print(A)

m = int(input("enter number top members to place in reverse position:\t"))

for i in range(0,n):
    if i < m :
        B.append(A[m-1-i])
    else:
        B.append(A[i])
print(B)

# temp1 = A.copy()
# for i in range(0,m):
#     temp1.pop(0)

# temp2 = A.copy()
# temp2.reverse()
# for i in range(0,n-m):
#     temp2.pop(0)
    
# temp2.extend(temp1)
# B = temp2

print(B)