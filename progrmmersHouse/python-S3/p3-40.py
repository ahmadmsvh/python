#Least Common Multiple #Greatest Common Divisor

number_one = int(input("\nenter a number:\t"))
number_two = int(input("\nenter a number:\t"))

if number_one > number_two:
    temp = number_one
    number_one = number_two
    number_two = temp
    
gcd = number_one + 1
gcd_flag = False

while gcd_flag == False and gcd > 1 :
    gcd -= 1
    if number_one % gcd == 0 :
        if number_two % gcd == 0 :
            gcd_flag = True
    
lcm = number_one - 1
lcm_flag = False

while lcm_flag == False and lcm < number_one * number_two :
    lcm += 1
    if lcm % number_one == 0 :
        if lcm % number_two == 0 :
            lcm_flag = True
    
print("(%d, %d)   gcd=%d    lcm=%d\n\n" %(number_one,number_two,gcd,lcm))