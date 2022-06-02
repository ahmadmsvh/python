# today = '2022-05-15'

# year,month,day = today.split('-')

# today_edited = '/'.join((year,month,day))

# print(today)
# print(today_edited)

# ############################################
# import numpy as np

# my_array = np.random.randint(low=5 , high= 10 ,size=10)
# print(my_array)

# print(type(my_array))
# print(dir(my_array))

# my_list = list(my_array)
# print(my_list)

# my_other_list = my_array.tolist()
# print(my_other_list)

# print(my_list.mean())
# print(my_other_list.mean())
# print(my_array.mean())

# print(dir(my_list))
# help(my_list.__add__)

############################################


my_array = [ [item,True] for item in range(20) if item%7 ==0 ]
my_array_c = [ [item,False] for item in range(20) if item%7 !=0 ]

result = sorted(my_array+my_array_c)

print(result)
