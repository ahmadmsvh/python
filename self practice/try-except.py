# def getNumber():
#     try:
#         number = int(input('enter a number:'))
#         return number
#     except Exception:
#         number = getNumber()
#         return number
        
# print(getNumber())


# print(dir(Exception))


try:
    inp = input('enter string:\t')

    if inp == 'zero':
        ahmad = Exception('wrong')
        raise ahmad
    if inp == 'one':
        hamid = Exception('bong')
        raise hamid

except Exception:
    print(ahmad.keys())