M = []
l = 0
counter = 0

for i in range(1,10000):
    counter = 0
    for x in M:
        counter += x.count(i)
    if counter == 0:
        sum_of_quoti_one = 0
        for j in range(1 , (i // 2) + 1):
            if i % j == 0:
                sum_of_quoti_one += j
        sum_of_quoti_two = 0
        for k in range(1 , (sum_of_quoti_one // 2) + 1):
            if sum_of_quoti_one % k == 0:
                sum_of_quoti_two += k 
        if i == sum_of_quoti_two and i != sum_of_quoti_one:
            M.append([0,0])
            M[l][0] = i
            M[l][1] = sum_of_quoti_one
            l += 1
for x in M:
    print(x)