array_mult = lambda x,y,z: x**y+z

print(array_mult(2,3,3))


array_mult = lambda x: x**2+1
mylist = [1,2,3,4,5]
print(list(map(array_mult,mylist)))


array_mult = lambda x,y,z: x**y+z
mylist1= [1,2,3,4,5]
mylist2= [1,2,3,4,5]
mylist3= [1,2,3,4,5]
print(list(map(array_mult,mylist1,mylist2,mylist3)))


array_mult = lambda x: x[0]**x[1]+x[2]
mylist= [[1,2,3],[2,2,3],[3,2,3],[4,2,3],[5,2,3]]
print(list(map(array_mult,mylist)))


mylist= [[1,2,3],[2,2,3],[3,2,3],[4,2,3],[5,2,3]]
print(list(map(lambda x: x[0]**x[1]+x[2],mylist)))


mylist= [[1,2,3],[2,2,3],[3,2,3],[4,2,3],[5,2,3]]
print(list(map(lambda x: 'big' if x[0]>2 else 'small',mylist)))


mylist= [[1,2,3],[2,2,3],[3,2,3],[4,2,3],[5,2,3]]
print(list(filter(lambda x: x[0]>2 ,mylist)))