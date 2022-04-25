invalid_flag = int(0)
num1=int(input("enter first number:\t"))
if num1 > 99:
    print("invalid number \"runagain\"")
    invalid_flag = 1

if invalid_flag == 0:
    num2=int(input("enter second number:\t"))
    if num2 > 99:
        print("invalid number \"runagain\"")
        invalid_flag = 1

    if invalid_flag == 0:
        digit11 = num1 % 10
        digit12 = num1 // 10
        max1 = digit11
        if digit12 > digit11:
            max1 = digit12

        digit21 = num2 % 10
        digit22 = num2 // 10
        max2 = digit21
        if digit22 > digit21:
            max2 = digit22

        if max1 > max2:
            print("selected number is %d"%num1)
        else:
            print("selected number is %d"%num2)

