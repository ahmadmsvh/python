f = open('08_Filing/my_file.txt', 'r')
print(f.readline(50))
f.readline(50)
f.readline(50)
print(f.readline(50))

f.close()

with open('08_Filing/my_file.txt', 'r') as fp:
    lines = fp.readlines()
print(lines)
print(lines[2])