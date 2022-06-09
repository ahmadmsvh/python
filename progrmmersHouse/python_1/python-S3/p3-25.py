n = int(input("\n\nenter n to calculate n(n-1)+...+3x4+2x1 serie:\t\n"))
result = 0

for i in range(1,n+1):
    result += i * (i+1)

print(result)