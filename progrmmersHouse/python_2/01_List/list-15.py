print("# 1------------------------------------------------")

l1 = [1,2,3]

l2 = l1

print(l2)

print(id(l1))
print(id(l2))

print("# 2------------------------------------------------")
l1 = [1,2,3]

l2 = l1
l1[0]= 7

print(l1)
print(l2)

print("# 3------------------------------------------------")
l1 = [1,2,3]
print(l1)

l2 = l1[:]
print(l2)

print(id(l1))
print(id(l2))

l1[0]=5
print(l1)
print(l2)

print("# 4------------------------------------------------")
l1 =[1,2,[7,8]]
l2 = l1[:]

print(l2)
l1[2][1]= 5

print(l1)
print(l2)

print(id(l1))
print(id(l2))

print(l1[2])
print(l2[2])

print(id(l1[2]))
print(id(l2[2]))


