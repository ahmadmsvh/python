a = int(input("A:\t"))
b = int(input("B:\t"))
c = int(input("C:\t"))

a1 = a % 10
b1 = b % 10
c1 = c % 10

a10 = (a // 10) % 10
b10 = (b // 10) % 10
c10 = (c // 10) % 10

if a10 > b10 and a10 > c10:
    if a1 > b1 and a1 > c1 :
        print("yes the number with greatest tens digit has the greatest ones digit")

if b10 > a10 and b10 > c10:
    if b1 > a1 and b1 > c1 :
        print("yes the number with greatest tens digit has the greatest ones digit")

if c10 > b10 and c10 > a10:
    if c1 > b1 and c1 > a1 :
        print("yes the number with greatest tens digit has the greatest ones digit")

