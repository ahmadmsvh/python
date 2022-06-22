import pickle

my_dict = {1:'1',2:'2',3:'3'}

with open('./08_Filing/my_dict.bin', 'wb') as fp:
    pickle.dump(my_dict, fp) # serialized list to file

with open('./08_Filing/my_dict.bin', 'rb') as fp:
    str = pickle.load(fp)
    print(str)

    print(my_dict == str)