my_dict = {'12a13':{'name':'azadeh','age':42}}
print(my_dict['12a13']['age'])

my_dict = {'name':'ahmad','job':'developer','age':33}

temp = my_dict['name']
del my_dict['name']
my_dict['fist name'] = temp

print(my_dict)
print('--------------------------')

names = ['ali','hasan','sam','soroush','taghi']
points = [100,90,85,65,95]
ages = [20,30,23,26,26]

mapped = zip(names,points,ages)

mapped = list(mapped)
print(mapped)


name,point,age = zip(*mapped)

print(list(name))
print(point)
print(age)

my_dict = {1:'one',2:'two',3:'three',4:'four'}
print(my_dict.setdefault(1))
print(my_dict)

print(my_dict.setdefault(3))
print(my_dict)

print(my_dict.setdefault(5))
print(my_dict)

print(my_dict.setdefault(7,'seven'))
print(my_dict)
