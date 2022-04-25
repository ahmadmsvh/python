input_number_one = int(input("\nenter a number:\t"))
input_number_two = int(input("\nenter a number:\t"))
input_number_three = int(input("\nenter a number:\t"))

even_counter = 0
odd_counter = 0
even_summation = 0
odd_summation = 0

if input_number_one % 2 == 0:
    even_counter += 1
    even_summation += input_number_one
else:
    odd_counter += 1
    odd_summation += input_number_one

if input_number_two % 2 == 0:
    even_counter += 1
    even_summation += input_number_two
else:
    odd_counter += 1
    odd_summation += input_number_two

if input_number_three % 2 == 0:
    even_counter += 1
    even_summation += input_number_three
else:
    odd_counter += 1
    odd_summation += input_number_three

if even_counter == 3 or odd_counter == 3 :
    print("yes\n")

if even_counter == 2 :
    if even_summation > odd_summation :
        print("yes\n")

if odd_counter == 2 :
    if odd_summation > even_summation :
        print("yes\n")