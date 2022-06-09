for i in range(100,1000):
    sum_of_digits = 0
    
    j = i
    while j > 0:
        remainder = j % 10
        sum_of_digits += remainder
        j //= 10
        
    prime_flag = True
    k = 2
    
    while prime_flag == True and k < sum_of_digits // 2 + 1 :
        if sum_of_digits % k == 0:
            prime_flag = False
        k += 1
    if prime_flag == True and sum_of_digits != 1:
        print("summation of digits of %d is %d that is a prime number" %(i,sum_of_digits))
            
        







    # for k in range (2,sum_of_digits // 2):
    #     if sum_of_digits % k == 0:
    #         prime_flag = False
    #         break
            
    # if prime_flag == True:
    #     print("summation of digits of %d is %d that is a prime number" %(i,sum_of_digits))    

    


