n = int(input("\nenter the n:\t"))
j = 1
series = 0

for i in range(1,n+1):
    j *= -1
    if j == -1:
        print("-4/%d "%(2 * i + 1),end = "")
    else:
        print("+4/%d "%(2 * i + 1), end = "")