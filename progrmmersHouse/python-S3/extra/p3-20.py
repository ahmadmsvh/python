max1=0
max2=0

for i in range(1,8):
	point = float(input("\nenter the point:\t"))
	if point > max1:
		max2 = max1
		max1 = point
	if  point > max2 and point < max1:
    		max2 = point	

print("second maximum point is %d" %max2)