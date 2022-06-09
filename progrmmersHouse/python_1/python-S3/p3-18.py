num = int(input("entr a number to consider its integer root:\t"))
i = 0

while i ** 2 <= num :
    i += 1

print("%d is the integer root of %d" %((i - 1),num))