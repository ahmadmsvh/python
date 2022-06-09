#Least Common Multiple #Greatest Common Divisor

number_one = int(input("\nenter a number:\t"))
number_two = int(input("\nenter a number:\t"))
number_three = int(input("\nenter a number:\t"))

if number_one > number_two:
    temp = number_two
    number_two = number_one
    number_one = temp

if number_one > number_three:
    temp = number_three
    number_three = number_one
    number_one = temp
    
if number_two > number_three:
    temp = number_three
    number_three = number_two
    number_two = temp

gcd = number_one + 1
gcd_flag = False

while gcd_flag == False and gcd > 1 :
    gcd -= 1
    if number_one % gcd == 0 :
        if number_two % gcd == 0 :
            if number_three % gcd == 0 :
                gcd_flag = True

print("\nmaximum packages is %d\n\n" %gcd)