import pickle

remove_name = input('enter a name to edit:\t')
phone_list =[]
with open('./08_Filing/phonBookBinary.bin', 'rb+') as fp:
    
    while True:
        try:
            person = pickle.load(fp)
            if person[0] != remove_name:
                phone_list.append(person)

        except EOFError:
            break

with open('./08_Filing/phonBookBinary.bin', 'wb') as fp:
    for person in phone_list:
        pickle.dump(person, fp)