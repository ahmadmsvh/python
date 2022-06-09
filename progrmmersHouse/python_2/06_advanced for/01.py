print('# 01 -------------------------------')

for char in 'python':
    print(char)

print('# 02 -------------------------------')

l = [(1,2),(3,4),(5,6)]
print(type(l))

for a,b in l:
    print(a,b)

print('# 03 -------------------------------')

l = [(1,2),(3,4),(5,6)]

for both in l:
    a,b = both
    print(a,b)

print('# 04 -------------------------------')

for a,*b,c in [(1,2,3,4),(5,6,7,8)]:
    print(a,b,c)

print('# 05 -------------------------------')

dict = { 'name':'ali', 'job':'engineer', 'age':39}

for key in dict:
    print(key)

print('# 06 -------------------------------')

for key, value in dict.items():
    print(key,value)


print('# 07 -------------------------------')

s = 'pythonprogramminglanguage'

for c in s[9:13]:
    print(c)

print('# 08 -------------------------------')

l = []

for x in range(5):
    l.append(x**2)

print(l)

print('# 09 -------------------------------')

print([x**2 for x in range(5)])

print('# 10 -------------------------------')

y = 7 

print([y*x for x in range(5)])

print('# 11 -------------------------------')

l = [(1,2),(3,4),(5,6)]
print([a+b for a,b in l])

print('# 12 -------------------------------')

print(list(zip(range(0,10,2),range(1,10,2))))
print([a*b for a,b in zip(range(0,10,2),range(1,10,2))])

print('# 13 -------------------------------')

s = 'python'

for i,v in enumerate(s):
    print('%s) %s ' %(i , v*7))

print('# 14 -------------------------------')

s = 'python'

print([v*i for i,v in enumerate(s)])

print('# 15 -------------------------------')

seasons = ['spring','summer','fall','winter']

print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))


print('# 16 -------------------------------')

lists = [[] for i in range(3)]

lists[0].append(8)
lists[1].append(12)
lists[2].append(1)

print(lists)


