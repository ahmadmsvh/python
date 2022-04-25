from array import array
import random

#--------------------------<< make an array >>--------------------------
def makeArray(index):
    input_arr = array("i", [0] * index)
    return input_arr

#--------------------------<< randomly fill an array >>--------------------------
def randInitArray(array_name):
    for i in range(0,len(array_name)):
        array_name[i] = random.randint(100,1000)
    return array_name

#--------------------------<< Main Program >>--------------------------
A = makeArray(50)
B = makeArray(50)
C = makeArray(50)

randInitArray(A)
randInitArray(B)

for i in range(0,50):
    if  A[i] > B[i]:
        C[i] = 1
    elif A[i] < B[i]:
        C[i] = -1
    else:
        C[i] = 0
        
print(C)

# import random
# A = []
# B = []
# C = []

# for i in range(0,50):
#     A.append(random.randint(1,10))

# for i in range(0,50):
#     B.append(random.randint(1,10))
    
# for i in range(0,50):
#     if A[i] > B[i]:
#         C.append(1)
#     elif A[i] < B[i]:
#         C.append(-1)
#     else:
#         C.append(0)

# for i in range(0,50):
#     print(A[i],B[i],C[i])