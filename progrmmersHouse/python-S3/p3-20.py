for i in range(7):
    point = float(input("\nenter the point:\t"))
    
    if i == 0:
        max1 = point
        max2 = point
    elif point > max1:
        max2 = max1
        max1 = point
    elif point < max1 and max2 == max1:     
        max2 = point    
    elif point < max1 and point >= max2:
        max2 = point
    
if max1 == max2:
    print("all gpas are equal")      
else:
    print("second maximum point is %d " %(max2))
