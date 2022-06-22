import pickle

with open('./08_Filing/phonBookBinary.bin', 'rb') as fp:
    
    while True:
        try:
            person = pickle.load(fp)
            print(person)
        except EOFError:
            break
