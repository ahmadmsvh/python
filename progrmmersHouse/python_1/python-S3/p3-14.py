num = 1

while num != 0:
    
    num = int(input("enter a number:\t"))
    if num == 0:
        break

    prime_flag = False
    i = 2
    
    while num % i != 0:
        if i > num //2 :
          prime_flag = True
          print("%d is a prime number"%num)
          break 
        i += 1
    
    if prime_flag == False:
        if num != 2:
            print("%d is not a prime number"%num)
        else:
            print("%d is a prime number"%num)

    # prime_flag = True
    # i = 1

    # while i < num//2 :
    #     i+=1
    #     if num % i == 0:
    #         print("%d is not a prime number"%num) 
    #         prime_flag = False
    #         break

    # if prime_flag == True:
    #     print("%d is a prime number"%num)
        

