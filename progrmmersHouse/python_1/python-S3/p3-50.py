# perfect_number_flag = False
# while perfect_number_flag == False:
#     number = int(input("enter a number:\t"))
#     sum = 0
#     for i in range(1, (number // 2) + 1):
#         if number % i == 0:
#             sum += i
#     if sum == number:
#         perfect_number_flag = True
#         print("it is a perfect number")
   
# for number in range (1,1000):
#     sum = 0
#     for i in range(1, (number // 2) + 1):
#         if number % i == 0:
#             sum += i
#     if sum == number:
#         print("%d is a perfect number"%number)

counter = 0    
number = 1
while counter < 5:
    sum = 0
    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            sum += i
    if sum == number:
        print("%d is a perfect number"%number)
    number += 1
    