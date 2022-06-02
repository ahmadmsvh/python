my_dict = {'name':'ahmad','number':123456}

my_dict['number'] = 345276

print(my_dict)

my_dict['address'] = 'tehran'

print(my_dict)

squares_dict = {1:1 , 2:4 , 3:8 , 4:16 , 5:32}
print(squares_dict.pop(4))
print(squares_dict)

print(squares_dict.popitem())
print(squares_dict)

squares_dict.clear()
print(squares_dict)

del squares_dict
print(squares_dict)