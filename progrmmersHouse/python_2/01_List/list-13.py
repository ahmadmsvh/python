pow_2 = [2 ** x for x in range(10)]
print(pow_2)

#------------------------------------------------
pow_2 = []
for x in range(10):
    pow_2.append(2**x)
print(pow_2)


pow_2 = [2 ** x for x in range(10) if x > 5]
print(pow_2)


odd = [x for x in range(20) if x%2==1]
print(odd)


print([x+y for x in ['python','c'] for y in ['language','programming']])
