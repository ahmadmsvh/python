with open('08_Filing/my_file.txt', 'r') as fp:
    lines = fp.readlines()

for line in lines:
    for char in line:
        if char == '3':
            print(line.strip())
