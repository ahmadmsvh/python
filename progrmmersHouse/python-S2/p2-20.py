num=float(input("enter your point: \t"))

if num<10:
    num*=1.2
    if num>9 and num<10:
        num=10

print("your final score is %f"%num)