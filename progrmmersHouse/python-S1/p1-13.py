print("counting tuna fish cans in boxes with 6 cans and remainings")

can_number=int(input("enter the number of cans:"))

remainings=can_number%6
box=(can_number-remainings)/6

print("there will be %d boxes and %d single cans" %(box,remainings))