my_file = None
try:
    my_file = open('08_Filing/my_file.txt', 'w') 

    my_file.write('hello world!')

except AttributeError:
    print('AttributeError')
finally:
    if my_file:
        my_file.close()

    

# my_file = open('08_Filing/my_file.txt', 'w') 

# my_file.write('hello world!')

# my_file.close()