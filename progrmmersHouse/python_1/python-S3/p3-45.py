# series = 2^1 + 2^2 + 2^3 + ... + 2^n

n = int(input("\nenter the n:\t"))
series = 0
for i in range(1 , n + 1):
    pow = 1
    for j in range(1 , i + 1):
        pow = pow * 2
        
    series = series + pow

print(series)






# serie = 0
# for i in range(1,n+1):
#     serie += 2 ** i
# print(serie)