def getNumber():
    try:
        return int(input('enter a number:'))
    except Exception:
        return getNumber()
        
print(getNumber())


print(dir(Exception))


try:
    inp = input('enter string:\t')

    if inp == 'zero':
        raise NameError 
    if inp == 'one':
        raise TypeError 
    print(inp)


except NameError as vd:
    print(type(vd))
except TypeError as ad:
    print(type(ad))