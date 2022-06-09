my_file = None
try:
    my_file = open('08_Filing/Payroll.txt', 'r') 

    table = my_file.readlines()

    print('Account'.ljust(10), 'Name'.ljust(10), 'Amount'.rjust(10))
    for record in table:
        columns = record.split()
        print(columns[0].ljust(10), columns[1].ljust(10), columns[2].rjust(10))
except AttributeError:
    print('AttributeError')
finally:
    if my_file:
        my_file.close()