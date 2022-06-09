counter = 0
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            if i == j or i == k or j == k :
                counter += 1
                print("%d position: (%d,%d,%d)" %(counter,i,j,k))
