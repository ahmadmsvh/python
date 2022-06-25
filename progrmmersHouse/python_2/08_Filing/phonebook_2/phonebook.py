import pickle


def mainMenu():
    try:
        option = (input('''

1. show all
2. add record
3. search
4. edit
5. delete
0. exit phonebook

enter your choice:\t'''))

        if option not in ['0','1','2','3','4','5']:
            print('\n-------not an option, please select from options--------')
            raise Exception
        return option
    except:
        return mainMenu()

def optionManager(option):
    if option == '1':
        showAll()
    elif option == '2':
        addRecord()
    elif option == '3':
        search()
    elif option == '4':
        edit()
    elif option == '5':
        delete()
    elif option == '0':
        exit()

def showAll():
    try:
        with open('./08_Filing/phonebook_2/phonebook.bin', 'rb') as fp:
            print('\n...........................\n')
            counter = 0
            record = pickle.load(fp)
            counter += 1
            print(record)
            while record:
                record = pickle.load(fp)
                counter += 1
                print(record)
        
            
    except:
        print('\n...........................\n')
        if counter == 0:
            print('\n-----there is no record in the phonebook------')

def addRecord():
    try:
        new_record = input('enter a record like "name : number" :\n\t')
        new_record = new_record.split(':')
        new_record = [new_record[0].strip(), new_record[1].strip()]
        new_record = new_record[0].ljust(10) + ' : ' + new_record[1].rjust(12)

        if new_record.split(':')[1].strip().isdigit():
            with open('./08_Filing/phonebook_2/phonebook.bin', 'ab') as fp:
                pickle.dump(new_record, fp)   
        else :
            raise Exception

    except:
        print('\n\nwrong input enter a valid record again\n')
        addRecord()

def search():
    name = input('\nplease enter the name:\t')
    with open('./08_Filing/phonebook_2/phonebook.bin', 'rb') as fp:
        try:
            while True:
                record = pickle.load(fp)
                if record.split(':')[0].strip() == name:
                    print('\n...........................\n')
                    print(record)
                    print('\n...........................\n')
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
                    new_record = new_record[0].ljust(10) + ' : ' + new_record[1].rjust(12)
                    new_phonebook.append(new_record)
                else:
                    new_phonebook.append(record)
                        
        except:
            print('\n----------------Deleted!--------------\n')
    
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

