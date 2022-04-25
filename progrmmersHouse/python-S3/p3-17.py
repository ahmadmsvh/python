num = int(input("entr a number to consider if it is a complete number:\t"))

for j in range(1,num):
    sum = 0
    for i in range(1, j // 2 + 1):
        if j % i == 0:
            sum += i
    if sum == j:
        print(j)

