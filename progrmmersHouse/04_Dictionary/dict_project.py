#-----------<< menu >>-----------
def menu():
    print('welcome to the Programmershouse dictionary\n\n\n')
    print('1: search')
    print('2: show all')
    print('3: edit')
    print('4: remove')
    print('5: add')
    print('enter any other number to exit')
    print()
    return int(input('select your choice:\t'))

#-----------<< searching >>-----------
def search():
    key = input('enter a word:\t')
    print('{} : {}'.format(key, dictionary[key]))
   

#-----------<< show all >>-----------
def showAll():
    for item in sorted(dictionary.items()):
        print('{} : {}'.format(item[0],item[1]))
       

#-----------<< adding or editing >>-----------
def edit():
    key = input('enter the word to add or edit:\t')
    dictionary[key] = input('enter mean of {}:\t'.format(key))

#-----------<< removing >>-----------
def remove():
    key = input('enter a word to remove from dictionary:\t')
    del dictionary[key]


#-----------<< Main Program >>-----------

dictionary = {'car':'mashin','apple':'sib',  'home':'khoone'}
menu_choice = 1 
while menu_choice in (1,2,3,4,5):
    menu_choice = menu()

    if menu_choice == 1:
        search()
    elif menu_choice == 2:
        showAll()
    elif menu_choice == 3:
        edit()
    elif menu_choice == 5:
        edit()
    elif menu_choice == 4:
        remove()

