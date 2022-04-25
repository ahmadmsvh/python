input_number = int(input("\nenter a positive integer number:\t"))
input_number_digit_counter = 0
i = input_number
while i > 0:
    i //= 10
    input_number_digit_counter += 1


range_min = 10 ** (input_number_digit_counter-1)
range_max = 10 ** (input_number_digit_counter)
prime_flag = False


while prime_flag == False:
    prime_flag = True
    i = 2
    while prime_flag == True and i < range_min // 2 :
        if range_min % i == 0:
            prime_flag = False
        i += 1
    if prime_flag == True:
        if range_min == 1:
            range_min = 2
        print("entered number is %d and desired prime number is %d" %(input_number,range_min))
    range_min += 1         