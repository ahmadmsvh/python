my_set = {1,3,5,7}

my_set.discard(5)
print(my_set)

my_set.remove(7)
print(my_set)

my_set.discard(2)
print(my_set)

# my_set.remove(2) # it raises keyError

my_set = set('HelloWord!')
print(my_set)

print(my_set.pop())
print(my_set)

my_set.clear()
print(my_set)

my_set_1 = {1,2,3,4,5}
my_set_2 = {4,5,6,7,8,9}
print(my_set_1 | my_set_2)

print(my_set_1.union(my_set_2))
print(my_set_2.union(my_set_1))

print(my_set_1 & my_set_2)

print(my_set_1.intersection(my_set_2))

print(my_set_1 - my_set_2)
print(my_set_2 - my_set_1)

print(my_set_1.difference(my_set_2))
print(my_set_2.difference(my_set_1))

print( 2 in my_set_1)
print( 2 not in my_set_1)


for letter in set('apple'):
    print(letter)

print(sum(my_set_1))

print(my_set_1 ^ my_set_2)      # (A - B) | (B -A)

A = {1,2,3,4,5}
B = {1,2,3}

print(A < B)
print(A > B)
print(A == B)
print(A is B)
print(A is not B)

