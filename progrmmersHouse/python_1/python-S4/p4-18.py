my_array = []

for i in range(10):
    my_array.append([])
    for j in range(5):
        my_array[i].append(int(input("enter row %d, columnn %d:\t" %(i,j))))

my_array_copy = my_array.copy()


while len(my_array_copy) > 0:
    equal_counter = my_array_copy.count(my_array_copy[0])
    zero_index_copy =  my_array_copy[0].copy()
    if equal_counter > 1:
        print(my_array_copy[0],"x", equal_counter)
    counter = 1
    while counter > 0 :
        my_array_copy.remove(zero_index_copy)
        counter = my_array_copy.count(zero_index_copy)
                     
for x in my_array_copy:
    for y in x:
        print(y,end="\t")
    print()