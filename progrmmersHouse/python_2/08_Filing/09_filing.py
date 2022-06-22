with open('./08_Filing/text.txt', 'rb') as fp:
    txt = fp.read()

    str = txt.decode('ascii')

    print(txt)
    print(str)