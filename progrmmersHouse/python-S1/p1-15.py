print("approximate the price of oranges")

orange_kilo=float(input("\nenter kg:\t"))
unit_price=float(input("\nenter the unit price:\t"))

price_high=orange_kilo*(unit_price+(unit_price*0.1))
price_low=orange_kilo*(unit_price-(unit_price*0.1))

print("\nthe price will be between %f and %f\n" %(price_low,price_high))
