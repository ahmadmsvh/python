def first(n):
    num = 0
    while num < n:
        yield num
        num += 2

for i in first(12):
    print(i)


