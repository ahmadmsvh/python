A = int(input("A:\t"))

counter = 1

A //= 10
if A > 0 :
    counter += 1

A //= 10
if A > 0 :
    counter += 1

A //= 10
if A >0 :
    counter += 1

A //= 10
if A > 0 :
    counter += 1

A //= 10
if A == 0 :
    print("it is a %d digit number"%counter)
else:
    print("this number have more than 5 digit")
    