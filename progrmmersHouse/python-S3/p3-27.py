for i in range(1,11):
    for j in range(1,11):
        result = i * j        
        if j == 10:
            print(result)
        else:
            if result < 10:
                print(result,end = "\t")
            else:
                print(result,end = "\t")
