marks = {}.fromkeys(['Python','C++','JAVA'], 10)
print(marks)

for item in marks.items():
    print(item)

for item in marks.keys():
    print(item)

for item in marks.values():
    print(item)

for item in marks:
    print(item)


marks_2 = {}.fromkeys(['python','c++','java'], [1,2,3])
print(marks_2)


squares = { x:x**2 for x in range(6)}
print(squares)



squares_2 ={}

for x in range(6):
    squares_2[x] = x**2

print(squares_2)
    

squares_3 = { x:x**2 for x in range(6) if x%2 == 0 }
print(squares_3)


squares_4 = {1:1, 3:9, 5:25, 7:49, 9:81}

print( 7 in squares_4)
print( 2 in squares_4)
print( 2 not in squares_4)

print('-----------------------')
squares_5 = {0:0, 2:4, 4:16, 6:36, 8:64}
print(squares_5)

print(all(squares_5))
print(any(squares_5))

print('-----------------------')
squares_6 = {}
print(squares_6)

print(all(squares_6))
print(any(squares_6))

print(len(squares_5),len(squares_6))


squares_5 = {'name':'ali', 'age':32, 'tel':'12345'}
squares_5 = sorted(squares_5)
# print(sorted(squares_5))
print(squares_5)