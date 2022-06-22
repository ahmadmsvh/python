import pickle

edit_name = input('enter a name to edit:\t')
new_number = input('enter new number:\t')

with open('./08_Filing/phonBookBinary.bin', 'rb+') as fp:
    
    while True:
        try:
            person = pickle.load(fp)
            position = fp.tell()
            if person[0] == edit_name:
                person[1] = new_number
                fp.seek(position-1,0)
                pickle.dump(person, fp)

        except EOFError:
            break

