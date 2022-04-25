side_one = float(input("enter first side:\t"))
side_two = float(input("enter second side:\t"))
side_three = float(input("enter third side:\t"))

side_three_max = side_one + side_two

while side_three >= side_three_max:
    side_three = float(input("enter a valid length it must be less than %d:\t"%side_three_max))
                 