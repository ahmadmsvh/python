n = int(input("\nenter the n number:\t"))
fibo_minus_one = 1
fibo_minus_two = 0
prime_flag = 1

if n > 1 :
    print(1)
for i in range(1,n):
    if n == 1:
        fibo = 1
    else:
        fibo = fibo_minus_one + fibo_minus_two
        fibo_minus_two = fibo_minus_one
        fibo_minus_one = fibo
    
    prime_flag = True
    i = 2
    while prime_flag == True and i < fibo // 2:
        if fibo % i == 0:
            prime_flag = False
        i += 1
    
    if prime_flag == True and fibo != 1:
        print(fibo,"\tprime")
    else:
        print(fibo)




        
        