import pickle

with open('./08_Filing/my_file.bin', 'wb') as fp:
    my_int = 12
    my_string = 'abbas'
    my_list = [1,2,3,4]
    my_dict = {'name':'ali', 'job':'teacher'}

    pickle.dump(my_int, fp)
    pickle.dump(my_string, fp)
    pickle.dump(my_list, fp)
    pickle.dump(my_dict, fp)

    