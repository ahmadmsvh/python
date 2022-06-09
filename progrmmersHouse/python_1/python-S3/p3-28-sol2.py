i = j = k = l = m = n = money = 0

for i in range(0,3):
    money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n)
    if money > 100:
        break
    if money == 100:
        print("50x%d  20x%d  10x%d  5x%d  2x%d  1x%d  "%(i,j,k,l,m,n))
        break
    for j in range(0,6):
        money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n) 
        if money > 100:
            j = 0
            break
        if money == 100:
            print("50x%d  20x%d  10x%d  5x%d  2x%d  1x%d  "%(i,j,k,l,m,n))
            j = 0
            break
        for k in range(0,11):
            money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n) 
            if money > 100:
                k = 0
                break
            if money == 100:
                print("50x%d  20x%d  10x%d  5x%d  2x%d  1x%d  "%(i,j,k,l,m,n))
                k = 0
                break
            for l in range(0,21):
                money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n) 
                if money > 100:
                    l = 0
                    break
                if money == 100:
                    print("50x%d  20x%d  10x%d  5x%d  2x%d  1x%d  "%(i,j,k,l,m,n))
                    l = 0
                    break
                for m in range(0,51):
                    money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n) 
                    if money > 100:
                        m = 0
                        break
                    if money == 100:
                        print("50x%d  20x%d  10x%d  5x%d  2x%d  1x%d  "%(i,j,k,l,m,n))
                        m = 0
                        break
                    for n in range(0,101):
                        money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n) 
                        if money > 100:
                            n = 0
                            break
                        if money == 100:
                            print("50x%d  20x%d  10x%d  5x%d  2x%d  1x%d  "%(i,j,k,l,m,n))
                            n = 0
                            break