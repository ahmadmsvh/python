import pickle

with open('./08_Filing/my_file.bin', 'rb') as fp:

    my_int = pickle.load(fp)
    my_string = pickle.load(fp)
    my_list = pickle.load(fp)
    my_dict = pickle.load(fp)

    print(my_int)
    print(my_string)
    print(my_list)
    print(my_dict)