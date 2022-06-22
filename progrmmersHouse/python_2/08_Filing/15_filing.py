import pickle

row_list_1 = ['ali', '091382839']
row_list_2 = ['vali','091284734']
row_list_3 = ['lili','092783902']

with open('./08_Filing/phonBookBinary.bin', 'wb') as fp:
    pickle.dump(row_list_1, fp)
    pickle.dump(row_list_2, fp)
    pickle.dump(row_list_3, fp)