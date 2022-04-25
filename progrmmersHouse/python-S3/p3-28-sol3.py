i = j = k = l = m = n = money = counter =0

while money <= 100 :
    while money <= 100 :
        while money <= 100 :
            while money <= 100 :
                while money <= 100 :
                    while money <= 100 :
                        if money == 100 :
                            print("50x%d  20x%d  10x%d  5x%d  2x%d  1x%d  "%(i,j,k,l,m,n))
                            counter += 1
                        n += 1
                        money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n)
                    n = 0    
                    m += 1
                    money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n)
                m = 0                
                l += 1
                money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n)
            l = 0            
            k += 1
            money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n)
        k = 0 
        j += 1
        money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n)
    j = 0
    i += 1
    money = (50 * i)  + (20 * j) + (10 * k) + (5 * l) + (2 * m) + (1 * n)    
print(counter)