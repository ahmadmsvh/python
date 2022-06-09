# 1. Show all
# 2. Search
# 3. Exit

# 4. Edit
# 5. Delete
# 6. Add new


# file (name, number)
with open('08_Filing/Telephone.txt', 'r') as fp:
    table = fp.readlines()

phone_book = {}

exit = False
while exit == False:
    print('1. Show all\n2. Search\n3. Exit\n')
    option = int(input('Pleas enter your choice:\t'))
  
    if option == 1:
        print('Name'.ljust(30), 'Number'.ljust(15))
        for record in table:
            items = record.split()
            print(items[0].ljust(30),items[1].ljust(15))
            print()
    elif option == 2:
        
        for record in table:
            items = record.split()
            phone_book[items[0]] = items[1]

        name = input('enter the name:\t')

        if name in phone_book:
            print(phone_book[name])
            print()
        else:
            print('the person does not exist')
            print()
            
    elif option == 3:
        exit = True