fp = open('./08_Filing/text.txt', 'r')

print('name of the file:\t', fp.name)

fp.seek(17,0)
line = fp.readline()
print(line)

fp.seek(0,1)
line = fp.readline()
print(line)

fp.seek(0,0)
line = fp.readline()
print(line)

fp.close()