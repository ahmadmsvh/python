number = int(input("\nenter a number to find the first prime number greater of that:\t"))
prime_flag = False

while prime_flag == False:
    number += 1
    
    prime_flag = True
    i = 2
    
    while prime_flag == True and i <= number // 2:
        if number % i == 0:
            prime_flag = False
        i += 1

print(number)