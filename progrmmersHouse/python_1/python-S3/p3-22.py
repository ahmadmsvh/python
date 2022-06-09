number = int(input("\n\nenter a number:\t"))
rebmun = 0

while number > 0:
    rem = number % 10
    number = number // 10
    rebmun= rebmun * 10 + rem
print (rebmun)
