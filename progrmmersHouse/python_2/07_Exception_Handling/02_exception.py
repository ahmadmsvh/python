try:
    age = int(input('enter your age:\t'))

    print(age)

except ValueError:
    print('you have entered invalid age!')

except KeyboardInterrupt:
    print('you cancelled the operation!')

except:
    print('something is wrong!')

else:
    if age <= 21:
        print('you are not allowed to enter!, you are too young.')
    else:
        print('welcome, you are allowed')