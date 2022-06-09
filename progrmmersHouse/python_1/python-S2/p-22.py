s1=float(input("enter side one:\t"))
s2=float(input("enter side two:\t"))
s3=float(input("enter side three:\t"))
s4=float(input("enter side four:\t"))

if s1==s2 and s3==s4:
    print("yes")
elif s1==s3 and s2==s4:
    print("yes")
elif s1==s3 and s2==s4:
    print("yes")
elif s1==s4 and s2==s3:
    print("yes")
else:
    print("no")
