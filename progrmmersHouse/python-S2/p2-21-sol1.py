point=int(input("enter the point:\t"))

point_five=0
point_three=0
point_one=0

if (point//5)>0:
    point_five=1
    point=point%5

if (point//3)>0:
    point_three=1
    point=point%3

if (point==1):
    point_one=1

print("five point:%d\tthree point:%d\tone point:%d"%(point_five,point_three,point_one))
