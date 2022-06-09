A = []
n = int(input("enter number of array members:\t"))

for i in range(n):
    A.append(int(input("enter A[%d]:\t" %i)))
print(A)

m = int(input("enter number top members to place in reverse position:\t"))

for i in range(m):
    A.insert(m-i,A[0])
    A.pop(0)

print(A)