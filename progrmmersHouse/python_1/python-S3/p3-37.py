for i in range(10,100):
    quotient = i
    summation_of_digits = 0
    
    while quotient > 0 :
        remainder = quotient % 10
        quotient = quotient // 10
        summation_of_digits += remainder

    if i % summation_of_digits == 0:
        print(i,end="  ")