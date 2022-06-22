fp = open('./08_Filing/Payroll.txt', 'r')

# fp.seek(5)  # file pointer 5 byte az avale file be jelo miravad

# fp.seek(5, 0)  # 5 byte az ebtedaye file
# fp.seek(5, 1)  # 5 byte az jaei ke file pointer boode
# fp.seek(5, 2)  # 5 byte az entehaye file

fp.seek(5)

print(fp.tell())
print(fp.readline())