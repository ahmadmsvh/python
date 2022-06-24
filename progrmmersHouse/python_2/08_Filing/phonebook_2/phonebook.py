import pickle


def mainMenu():
    try:
        option = int(input('''

    1. show all
    2. add record
    3. search
    4. edit
    5. delete

    enter your choice:\t'''))

        if option not in [0,1,2,3,4,5]:
            print('\n\tnot an option, please select from options:')
            raise Exception
        return option
    except:
        return mainMenu()

def optionManager(option):
    if option == 1:
        addRecord()
    elif option == 2:
        showAll()
    elif option == 3:
        search()
    elif option == 4:
        edit()
    elif option == 5:
        delete()
    elif option == 0:
        exit()

def addRecord():
    try:
        new_record = input('enter a record like "name" : "number" :\n\t')
        new_record = new_record.split(':')
        new_record = [new_record[0].strip(), new_record[1].strip()]
        new_record = new_record[0] + ' : ' + new_record[1]

        if new_record.split(':')[1].strip().isdigit():
            with open('./08_Filing/phonebook_2/phonebook.bin', 'ab') as fp:
                pickle.dump(new_record, fp)   
        else :
            raise Exception

    except:
        print('\n\n wrong input enter a valid record again\n')
        addRecord()

def showAll():
    try:
        with open('./08_Filing/phonebook_2/phonebook.bin', 'rb') as fp:
            counter = 0
            record = pickle.load(fp)
            counter += 1
            print(record)
            while record:
                record = pickle.load(fp)
                counter += 1
                print(record)
    except:
        if counter == 0:
            print('\nthere is no record in the phonebook')

def search():
    name = input('\nplease enter the name:\t')
    with open('./08_Filing/phonebook_2/phonebook.bin', 'rb') as fp:
        try:
            while True:
                record = pickle.load(fp)
                if record.split(':')[0].strip() == name:
                    print(record)
                    break
        except:
            print('\n-------person not found-------\n')

def edit():
    name = input('\nplease enter the name:\t')
    new_phonebook = []
    with open('./08_Filing/phonebook_2/phonebook.bin', 'rb') as fp:
        try:
            while True:
                record = pickle.load(fp)
                if record.split(':')[0].strip() == name:
                    new_record = input('enter a record like "name" : "number" :\n\t')
                    new_record = new_record.split(':')
                    new_record = [new_record[0].strip(), new_record[1].strip()]
                    new_record = new_record[0] + ' : ' + new_record[1]
                    new_phonebook.append(new_record)
                else:
                    new_phonebook.append(record)
                        
        except:
            print('\n-------person not found-------\n')
    
    with open('./08_Filing/phonebook_2/phonebook.bin', 'wb') as fp:
        for record in new_phonebook:
            pickle.dump(record, fp)

def delete():
    name = input('\nplease enter the name:\t')
    new_phonebook = []
    with open('./08_Filing/phonebook_2/phonebook.bin', 'rb') as fp:
        try:
            while True:
                record = pickle.load(fp)
                if record.split(':')[0].strip() != name:
                    new_phonebook.append(record)
                        
        except:
            print('\n-------person not found-------\n')
    
    with open('./08_Filing/phonebook_2/phonebook.bin', 'wb') as fp:
        for record in new_phonebook:
            pickle.dump(record, fp)


#---------------<< Main Program >>---------------

while True:

    option = mainMenu()

    optionManager(option)

