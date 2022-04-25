num = float(input("enter a number:\t"))
sum = 0
counter = 0
average = 0

while num != 0:
    counter += 1
    sum += num
    num = float(input("enter a number:\t"))
    
if counter > 0 :
    average = float(sum/counter)

print(average)