even_counter = 0 
counter_three = 0
counter = 0

while even_counter < 4:
    if counter == 10:
        break
    num = int(input("enter %dth number:\t"))
    counter += 1
    if num % 2 == 0:
        even_counter += 1
        if num % 3 == 0:
            counter_three += 1

print(counter_three)


