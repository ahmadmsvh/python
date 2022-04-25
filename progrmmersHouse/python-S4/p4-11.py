my_array = ["A","B","C","D","E","F","G","H","I"]
print(my_array)

k = int(input("enter a number less than %d:"%len(my_array)))

for i in range(0,k):
    my_array.append(my_array[0])
    my_array.pop(0)
    
print(my_array)
    