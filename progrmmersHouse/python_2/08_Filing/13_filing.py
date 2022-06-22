import os

if os.path.exists('./08_Filing/my_file.bin'):
    os.remove('./08_Filing/my_file.bin')
else:
    print('this file does not exist')