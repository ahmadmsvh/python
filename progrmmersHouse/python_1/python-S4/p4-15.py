myArray = []

for i in range(3):
    myArray.append([])
    for j in range(4):
        myArray[i].append(".")

inp = str(input("enter something:\t"))
i = int(input("enter row position:\t"))
j = int(input("enter column position:\t"))

myArray[i][j] = inp

for x in myArray:
    for y in x:
        print(y,end="\t")
    print()    
    