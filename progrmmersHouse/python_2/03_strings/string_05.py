str_1 = "{}, {} and {}".format('ali','emad','sam')
print(str_1)


str_1 = "{1}, {0} and {2}".format('ali','emad','sam')
print(str_1)


str_1 = "{s}, {d} and {k}".format(s='ali',k='emad',d='sam')
print(str_1)

str_2 = "binary {0} is {0:b},{0:x},{0:o} ".format(12)
print(str_2)


str_3 = "{0:e} ".format(1024.232)
print(str_3)


str_4 = "{0:f}".format(1/3)
print(str_4)


str_4 = "{0:.3f}".format(1/3)
print(str_4)


x = 12.34556789
print("value of x is %3.2f" %x)


x = 12.34556789
print("value of x is %3.4f" %x)