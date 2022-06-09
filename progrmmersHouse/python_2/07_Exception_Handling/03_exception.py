try:
    a = float(input('enter a float number 1:\t'))
    b = float(input('enter a float number 2:\t'))

    c = a / b
except ValueError:
    print('you have entered invalid number')

except ZeroDivisionError:
    print('you have an divide by zero error!')

except:
    print('somrthing is wrong')

else:
    print(c)


