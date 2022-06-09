point_flag = False
while point_flag == False:
    point = float(input("enter your point:\t"))
    if 20 > point > 0 :
        point_flag = True
print("your point is %d" %point)