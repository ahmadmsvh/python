import pickle

new_number = []
new_number.append(input('enter new name:\t'))
new_number.append(input('enter number:\t'))

with open('./08_Filing/phonBookBinary.bin', 'ab') as fp:
    pickle.dump(new_number, fp)


with open('./08_Filing/phonBookBinary.bin', 'rb') as fp:
    
    while True:
        try:
            person = pickle.load(fp)
            print(person)
        except EOFError:
            break