#--------------------------------
def openPhoneBook():
    phone_book_name = input('\nenter phone book name (enter 0 to go to previous menu):\t')
    
    phone_book = findPhoneBook(phone_book_name)
    if phone_book == None:
        return

    
    while True:            
        print('________________________________________________')
        print('\n\tenter "1" to show all.')
        print('\n\tenter "2" to find number.')
        print('\n\tenter "3" to add a number.')
        print('\n\tenter "4" to remove a number.')
        print('\n\tenter "0" to go to previous menu.')
        print('________________________________________________')

        options = [1,2,3,4,0]

        option = getOption(options)

        if option == 1:
            phone_book_dict = {}
            for line in phone_book.readlines():
                phone_book_dict['{}'.format(line.split(':')[0].strip())] = line.split(':')[1].strip()

            for person in phone_book_dict:
                print(person, ' : ', phone_book_dict[person])
        elif option == 2:
            person = findPerson(phone_book_dict)
        elif option == 3:
            phone_book.close()
            phone_book = addPerson(phone_book_name)
        elif option == 4:
            phone_book = removePerson(phone_book_name)
        elif option == 0:
            phone_book.close()
            return

#--------------------------------
def findPerson(phone_book_dict):
    name = input('\n\tenter the name:\t')
    if name not in phone_book_dict:
        print('\nperson does not exist!!!')
    else:
        print(name,' : ',phone_book_dict[name])
        

#--------------------------------    
def findPhoneBook(phone_book_name):
    try:
        if phone_book_name == '0':
            return 
        fp = open('./08_Filing/{}.txt'.format(phone_book_name), 'r')
        return fp
    except FileNotFoundError:
        print('phone book does not exist!!!')
        return openPhoneBook()

#--------------------------------
def addPerson(phone_book_name):
    fp = open('./08_Filing/{}.txt'.format(phone_book_name), 'a')
    new_number = input('enter new name and number like (name:number) :\t')
    fp.write(new_number+'\n')
    print('\n\t"new number added"')
    fp.close()
    fp = open('./08_Filing/{}.txt'.format(phone_book_name), 'r')
    return fp

#--------------------------------
def removePerson(phone_book_name):
    fp = open('./08_Filing/{}.txt'.format(phone_book_name), 'r')

    phone_book_dict = {}

    for line in fp.readlines():
        phone_book_dict['{}'.format(line.split(':')[0].strip())] = line.split(':')[1].strip()

    remove_name = input('\n\tenter a name to remove:\t')
    phone_book_dict.pop(remove_name)

    new_string = ''
    for item in phone_book_dict:
        new_string += '{}:{}\n'.format(item,phone_book_dict[item])
    
    fp.close()
    
    fp = open('./08_Filing/{}.txt'.format(phone_book_name), 'w')
    fp.write(new_string)
    fp.close()

    fp = open('./08_Filing/{}.txt'.format(phone_book_name), 'r')
    return fp

#--------------------------------
def createPhonBook():
    pass

#--------------------------------
def removePhoneBook():
    pass

#--------------------------------
def getOption(options):
    try:
        option = int(input('enter your choice:\t'))
        if option not in options:
            raise Exception
        return option
    except:
        print('\n\t"invalid option"')
        return getOption(options)

#----------------<< Main Program >>----------------

while True:
    print('________________________________________________')
    print('\n\tenter "1" to open a phone book.')
    print('\n\tenter "2" to create a phone book.')
    print('\n\tenter "3" to remove a phone book.')
    print('\n\tenter "0" to exit.')
    print('________________________________________________')

    options = [1,2,3,0]

    option = getOption(options)

    if option == 1:
        openPhoneBook()
    elif option == 2:
        createPhonBook()    
    elif option == 3:
        removePhoneBook()
    elif option == 0:
        exit()