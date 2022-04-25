from array import array

#--------------------------<< make an array >>--------------------------
def makeArray(index):
    input_arr = array("i", [0] * index)
    return input_arr

#--------------------------<< Prime Number >>--------------------------
def isPrime(number):
    for i in range(2,number // 2 + 1):
        if number % i == 0:
            return False
    return True

#--------------------------<< Show Prime Numbers Less Than >>--------------------------
def showPrimes(number):
    result = makeArray(0)
    for i in range(2,number):
        if isPrime(i) == True:
            result.append(i)
    return result

#--------------------------<< Main Program >>--------------------------
number = int(input("enter a number : \t"))
result = showPrimes(number)
print(result)




# number = int(input("entr a number:\t"))
# num_array = []

# for i in range(2,number):
#     prime_flag = True
#     j = 2
#     while prime_flag == True and j <= (i // 2):
#         if i % j == 0:
#             prime_flag = False
#         j += 1
#     if prime_flag == True:
#         num_array.append(i)

# print(num_array)
