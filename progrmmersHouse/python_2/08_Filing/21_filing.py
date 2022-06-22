import shutil

source = './08_Filing/text.txt'
destination = './08_Filing/text_2.txt'

try:
    shutil.copy(source,destination)
except shutil.SameFileError:
    print('source and destination are the same')