weight=float(input("enter the weight of bananas:\t"))
unit_price=float(input(" enter unit price:\t "))

unit_price_off_5=unit_price*0.95
unit_price_off_20=unit_price*0.90

if weight>=20:
    price=weight*unit_price_off_20
elif weight>=5:
    price=weight*unit_price_off_5
else:
    price=weight*unit_price

print("please pay:\t%f$"%price)


