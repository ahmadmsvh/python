import copy 
a = [[1,2],[3,4]]
b = copy.copy(a)
c = copy.deepcopy(a)

print(a)
print(b)
print(c)

print(id(a[0]))
print(id(a[0][0]))

print(id(b[0]))
print(id(b[0][0]))

print(id(c[0]))
print(id(c[0][0]))