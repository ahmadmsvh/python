import random

n = int(input("enter number of array max:\t"))
m = int(input("enter shift number:\t"))
direction = str(input("left or right:\t"))

my_array = []

for i in range(n):
    my_array.append(random.randint(0,99))

temp = 0
print(my_array)

if direction == "right":
    for i in range(m):
        temp = my_array[n-1]
        for j in range(n-1,0,-1):
            my_array[j] = my_array[j-1]
        my_array[0] = temp
            
    print(my_array)

elif direction == "left":
    for i in range(m):
        temp = my_array[0]
        for j in range(0,n-1):
            my_array[j] = my_array[j+1]
        my_array[n-1] = temp
            
    print(my_array)