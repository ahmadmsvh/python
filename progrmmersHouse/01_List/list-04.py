#-----List Slicing------

my_list = ['p','r','o','g','r','a','m','m','e','r','s','h','o','u','s','e']

print(my_list[2:5]) # ['o','g','r']

print(my_list[5:]) 

print(my_list[:])

print(my_list) 

#------------------------------------
l = ['spam','Spam','SPAM']
l[1]='eggs'
print(l)


l[0:2] = ['eat','more']
print(l)

del(l[0])
print(l)

del(l[1:])
print(l)

print('------------------------')

#------------------------------------
shop_list = ['apple','mango','carrot','banana']

print(shop_list[::1])

print(shop_list[::2])

print(shop_list[::3])

print(shop_list[::-1])


