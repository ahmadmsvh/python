import random

my_array = []

for i in range(100):
    my_array.append(random.randint(0,99))

max = 1
for x in my_array:
    counter = my_array.count(x)
    if counter > max :
        max = counter
        max_content = x
        
print("%d  x  %d" %(max_content,max))
print(my_array)