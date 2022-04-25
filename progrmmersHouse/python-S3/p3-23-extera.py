number = int(input("enter  number:\t"))
q = number
digit_counter = 0

while (q > 0):
      q = q // 10
      digit_counter += 1

digit = digit_counter
sum = 0
q = number

while (q > 0 ):
    rem = q % 10
    q = q // 10
    tenpower = 1
    for i in range(1,digit):
        tenpower *= 10
    digit -= 1     
    sum += rem * tenpower

if sum == number:
    print("palindrome")  
else:
    print("not polindrome") 



