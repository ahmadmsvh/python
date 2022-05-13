import sys 

zoo_tuple = ('lion','python','eagle','penguin','mouse')
print('1--------------------------')
print(len(zoo_tuple))

new_zoo_tuple = 'lion','python','eagle','penguin','mouse',zoo_tuple


print('2--------------------------')
print(type(new_zoo_tuple))
print(len(new_zoo_tuple))
print(new_zoo_tuple[5][1])
print(len(new_zoo_tuple)-1 + len(new_zoo_tuple[-1]))
print(len(new_zoo_tuple)-1 + len(zoo_tuple))

print('3--------------------------')
my_tuple = (1,'a')
my_list = [1,'a']
print(sys.getsizeof(my_tuple))
print(sys.getsizeof(my_list))

print('4--------------------------')
t = 5>2,True == 0, 7-2
print(type(t))
print(t)

print('5--------------------------')
print((1,'python')==(1,'python'))
print((1,'python')==(1,'Python'))

t1 = (1,2,3)
t2 = t1
print(id(t1),id(t2))
print(t1 == t2)
print(t1 is t2)

t1 = (1,2,3)
t2 = (1,2,3)
print(t1 == t2)
print(t1 is t2)
print(id(t1),id(t2))

print('6--------------------------')

a,*b =(1.1,2.2,3.3,4.4)
print(a)
print(b)
print(type(a),type(b))

a,*b,c = (1.1,2.2,3.3,4.4)
print(a)
print(b)
print(c)
print(type(a),type(b),type(c))

a,*b = [1.1,2.2,(3.3,4.4)]
print(a)
print(b)
print(type(a),type(b))


a,b,*c = [1.1,2.2,(3.3,4.4)]
print(a)
print(b)
print(c)
print(type(a),type(b),type(c))


print('7--------------------------')
list1 = [1.1,2.2,(3.3,4.4)]
# list1[2][0] = 1
print(list1)

print('8--------------------------')
my_tuple = ('p','y','t','h','o','N')
print(sorted(my_tuple, key = str.lower, reverse =True ))
print(type(sorted(my_tuple, key = str.lower, reverse =True )))

my_tuple = sorted(my_tuple, key = str.lower, reverse =True )
print(my_tuple)

print('9--------------------------')
t = (1,2,3)
print(type(t))

l = list(t)
l.insert(1,12)
print(l)

t = tuple(l)
print(t)
