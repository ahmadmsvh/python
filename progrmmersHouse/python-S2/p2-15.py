num=int(input("enter the number:\t"))

num_copy=num

digit1=num_copy%10
num_copy=num_copy//10
digit2=num_copy%10

if digit1%2==0 and digit2%2==0:
    print("this is the desired number")
else:
    print("it is not desired")