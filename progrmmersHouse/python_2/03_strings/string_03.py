my_string = 'hello world'

print(my_string.count('l'))

counter = 0

for letter in my_string:
    if letter == 'l':
        counter += 1
print(counter)

print('w' in my_string)
print('z' not in my_string)
print(len(my_string))

str_1 = 'cold'

list_enumerate = (enumerate(str_1))
print(list_enumerate)

list_enumerate = list(enumerate(str_1))
print(list_enumerate)

list_enumerate_2 = list(enumerate(str_1,2))
print(list_enumerate_2)

print(list(enumerate(list_enumerate_2)))

for i in enumerate(list_enumerate_2):
    print(i)

for i,j in enumerate(list_enumerate_2):
    print(i)
    print(j)

for i in list_enumerate_2:
    print(i[0])

print('\n4-------------------------\n')
for i in (str_1):
    print(i)


print('\n5----------------------------\n')
index =2
values = ['a','b','c']

for value in values:
    print(index,value)
    index += 1

print('\n6----------------------------\n')

values_enumarated = list(enumerate(values,2))
for item in values_enumarated:
    print(item)

employees = ['mousavi','abdipour','bachari','yousefi','piri']
for index,employee in enumerate(employees,10):
    if index == 13:
        print(employee)