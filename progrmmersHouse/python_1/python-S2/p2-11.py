print("enter 3 numbers to make a triangle and recognize type of that")
side_one=float(input("enter side one:\t"))
side_two=float(input("enter side one:\t"))
side_three=float(input("enter side one:\t"))

if not(side_one+side_two>side_three and side_one+side_three>side_two and side_two+side_three>side_one) :
    print('"entered values are not valid"')
elif side_one==side_two==side_three:
    print('"this is an equilateral triangle"')
elif side_one==side_two or side_one==side_three or side_two==side_three:
    print('"this is an isosceles triangle"')







    



