number = int(input("\n\nenter a number:\t"))
rebmun=0

while number > 0:
    rem = number % 10
    number = number // 10
    rebmun= rebmun * 10 + rem
    
if rebmun == number :
    print("this is a Palindrome number\n\n")
else:
    print("this is not a Palindrome number\n\n")
