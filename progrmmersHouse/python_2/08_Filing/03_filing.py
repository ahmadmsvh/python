f = open('08_Filing/my_file.txt', 'r')
print(f.readline())

f.close()

with open('08_Filing/my_file.txt', 'r') as fp:
    lines = fp.readlines()

print(lines[2])