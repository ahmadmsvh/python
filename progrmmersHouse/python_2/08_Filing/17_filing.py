import pickle

search = 'ali'

with open('./08_Filing/phonBookBinary.bin', 'rb') as fp:
    
    while True:
        try:
            person = pickle.load(fp)
            if person[0] == search:
                print(person)
        except EOFError:
            break