print(" imagine a number between 1 and 1000000 and I will tell you what it is through 20 questions")
max=float(1000000)
min=float(0)
answer=""
i = 1

while answer!= 0 and i <= 20 :
    var = min+(max-min)/2
    answer = str(input("\n#%d: if number = %d enter 0, if number > %d enter 1 else enter 2:\t" %(i,var,var)))
    if answer == "1":
        max = max
        min = var
    elif answer == "2":
        max = var
        min = min
    i += 1
print("your imagined number is %d\n\n" %var)    