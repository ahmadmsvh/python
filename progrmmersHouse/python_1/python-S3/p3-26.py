counter = 0

for i in range(100,201,4):
    
    if i % 10 == 0:
        counter += 1
        print(i,end="  ")
    elif i % 10 == 2:
        counter += 1
        print(i,end="  ")
    
print(counter)
