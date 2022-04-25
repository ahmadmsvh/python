a = int(input("A:\t"))
b = int(input("B:\t"))
c = int(input("C:\t"))
d = int(input("D:\t"))

counter = int(0);
position = int(0);

if a  > 10 :
    counter += 1
    position = 1 
elif a + b > 10:
    counter += 1
    position = 2
elif a + b + c > 10 :
    counter += 1
    position = 3
elif a + b + c + d > 10 :
    counter += 1
    position = 4

if position == 1:
    if b  > 10 :
        counter += 1
        position = 2
    elif b + c > 10:
        counter += 1
        position = 3
    elif b + c + d > 10 :
        counter += 1;
        position = 4

if position == 2:
    if c > 10 :
        counter += 1
        position = 3
    elif c+ d > 10:
        counter += 1
        position = 4
    
if position == 3:
    if d > 10 :
        counter += 1
        position = 4
    
print("maximum of GREATER THAN 10 packages is %d"%counter)
