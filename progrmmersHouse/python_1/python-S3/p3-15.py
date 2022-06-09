for i in range(100,1000):
    prime_flag = True
    j = 2
    
    while prime_flag == True and j < i // 2:
        if i % j == 0 :
            prime_flag = False
        j += 1
    
    if prime_flag == True:
        print(i)
            
    












# prime_flag = True

# for num in range(100,1000):
#     prime_flag = True
#     i = 2
    
#     while prime_flag == True and i < num // 2:
#         if num % i == 0:
#             prime_flag = False
#         i += 1
            
#     if prime_flag == True:
#         print(num)
        
        # print(num , end = " "),
