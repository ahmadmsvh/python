squares = {'name':'ali', 'age':32, 'tel':'12345'}

del squares['age']

print(squares)

my_dict = {'ahmad':'ahmad@gmail.com','bachari':'bachari@gmail.com','vahid':'vahid@gmail.com'}

for name,email in my_dict.items():
    print('contanct {} at {}'.format(name,email))


my_dict_2 = {1:'one',2:'two',3:'three',4:'four'}
my_dict_3 = {5:'five',7:'seven'}

my_dict_3.update(my_dict_2)
print(my_dict_2)
print(my_dict_3)


product = {'tea':10000,'milk':12000,'bread':3000,'oil':23000}
product_old = product
product_new = {'water':36000,'milk':18000,'oil':105000}

product.update(product_new)
print(product)

my_list = [[1980,4],[1990,24],[2000,34]]
my_dict = dict(my_list)
print(my_dict)


my_dict_backup = my_dict.copy()
print(my_dict_backup)


my_dict_2 = {1:'one',2:'two',3:'three',4:'four'}
# print(my_dict_2[0])
print(my_dict_2[1])
print(my_dict_2[3][2:])

