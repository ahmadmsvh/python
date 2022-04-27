import string
import random

def makeRandmArray():
    row = random.randint(3,9)
    col = random.randint(3,9)

    rand_array = [[random.choice(string.printable) for x in range(col)] for x in range(row)]

    return rand_array

# print(list(string.ascii_letters))

rand_array = makeRandmArray()
for x in rand_array:
    print(x)
print()

for row in range(len(rand_array)):
    for col in range(len(rand_array[0])):
        if rand_array[row][col] in list(string.ascii_lowercase):
            rand_array[row][col] = rand_array[row][col].upper()
        elif rand_array[row][col] in list(string.ascii_uppercase):
            rand_array[row][col] = rand_array[row][col].lower()
        elif rand_array[row][col] in list(string.digits):
            rand_array[row][col] = '0'
        else:
            rand_array[row][col] = '*'

for x in rand_array:
    print(x)

        