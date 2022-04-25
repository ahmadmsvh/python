a = int(input("A:\t"))
b = int(input("B:\t"))

aa = a % 100
if aa > 50:
    aa = 100 - (a % 100) 


bb = b % 100
if bb > 50:
    bb = 100 - (b % 100)

if aa < bb :
    print("a: %d"%a)

if bb < aa :
    print("b: %d"%b)
else:
    print("b: %d"%b)