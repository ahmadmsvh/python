n = int(input("enter a number:\t"))

f1 = 0
f2 = 1
f3 = 1

for i in range(1,n):
    f3 = f1 + f2
    f1 = f2
    f2 = f3
print(f3)
        
        

# n = int(input("enter the desired number of fibbonacci sequence:\t "))

# fib_n_minus_one = 1
# fib_n_minus_two = 1
# fib_n = 0

# if n == 1  or n == 2:
#     fib_n = 1

# for i in range(2,n):
#     fib_n = fib_n_minus_one + fib_n_minus_two
#     fib_n_minus_two = fib_n_minus_one
#     fib_n_minus_one = fib_n

# print("%dth sequence of fibbonacci serie is %d"%(n,fib_n))