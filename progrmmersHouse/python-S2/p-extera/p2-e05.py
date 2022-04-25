rials=float(input("enter amount of money in rials to convert:\t"))
currency=input('enter "d" for DOLLAR, "e" for EURO, "p" for POUND:\t')

dollar=rials/270000
euro=rials/320000
pound=rials/360000

if currency=="d" or currency=="D" :
    print("dollar:\t%f" %dollar)
if currency=="e" or currency=="E":
    print("euro:\t%f" %euro)
if currency=="p" or currency=="P":
    print("euro:\t%f" %pound)