input_number = int(input("enter a number greater than 99:\t"))
if input_number < 100 :
    print("invalid number")
else:
    input_number = input_number // 10
    tens_digit = input_number % 10

    input_number = input_number // 10
    hundreds_digit = input_number % 10

    sum = tens_digit + hundreds_digit

    print("summation =%d"%sum)