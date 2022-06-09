f = open('08_Filing/my_file.txt', 'r')
for line in f:
    print(line)

f.close()

with open('08_Filing/my_file.txt', 'r') as fp:
    for line in fp:
        print(line)
        