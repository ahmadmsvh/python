print("calculating the unused iron mass")

square_length=float(input("enter the length of square:\t"))

square_surface=square_length**2
total_mass=square_surface*20
circle_surface=3.14*((square_length/2)**2)
unused_iron_mass=(square_surface-circle_surface)*20

print("total iron mass is:\t%f" %total_mass)
print("unused iron mass is:\t%f" %unused_iron_mass)