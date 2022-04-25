import random
rand_array = []

for i in range(100):
    rand_array.append(random.randint(0,99))
print(rand_array)

i = 0
while len(rand_array) > 0:
    temp = rand_array[0]
    i += rand_array.count(rand_array[0])
    print("%d\t ---> %d" %(temp,rand_array.count(rand_array[0])))
    while rand_array.count(temp) > 0 :
        rand_array.remove(temp)
print(i)