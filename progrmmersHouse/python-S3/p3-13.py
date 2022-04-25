num = int(input("enter a number:\t"))

j = 0

half_num = num//2 

for i in range(3,half_num):   
    if num % i == 0:
        print("this number is not prime\n")
        j = 1
        break
if j == 0 :
    print("%d is a prime number\n" %num)