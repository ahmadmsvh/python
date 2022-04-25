#Least Common Multiple #Greatest Common Divisor

is_seen_gcd = False
i = 1

while is_seen_gcd == False:
    if 10 % i == 0:
        if 15 % i == 0:
            is_seen_gcd = True
            gcd_10_15 = i
    i -= 1
    
lcm_10_15 = 10 * 15 / gcd_10_15

is_seen_gcd = False

if lcm_10_15 > 25:
    less = 25
    great = lcm_10_15
else:
    less = lcm_10_15
    great = 25

i = less
while is_seen_gcd == False:
    if less % i == 0 :
        if great % i == 0 :
            is_seen_gcd = True
            gcd_25 = i
    i -= 1

lcm = less * great / gcd_25
print(lcm)


# number_one = int(input("\nenter a number:\t"))
# number_two = int(input("\nenter a number:\t"))
# number_three = int(input("\nenter a number:\t"))

# if number_one > number_two:
#     temp = number_two
#     number_two = number_one
#     number_one = temp

# if number_one > number_three:
#     temp = number_three
#     number_three = number_one
#     number_one = temp
    
# if number_two > number_three:
#     temp = number_three
#     number_three = number_two
#     number_two = temp

# lcm = number_three - 1
# lcm_flag = False

# while lcm_flag == False and lcm < number_one * number_two * number_three :
#     lcm += 1
#     if lcm % number_one == 0 :
#         if lcm % number_two == 0 :
#             if lcm % number_three == 0 :
#                 lcm_flag = True
    
# print("\nall the buses will meet again after %d minutes\n" %lcm)