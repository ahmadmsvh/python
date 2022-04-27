def getNumber():
    try:
        number = int(input('enter a number:'))
        return number
    except Exception:
        number = getNumber()
        return number
        
print(getNumber())