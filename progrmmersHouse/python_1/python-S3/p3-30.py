number = int(input("\nenter a number:\t"))
q = number
rem = 0
accum = 0

while q > 0:
    rem = q % 10
    q = q // 10
    for i in range(1 , rem * 2 , 2):
        accum += i

print("\n%d\n"%accum)