import datetime

birth_date = input()
birth_date = birth_date.split('/')

try:
    birth_date = datetime.datetime(int(birth_date[0]),int(birth_date[1]),int(birth_date[2]))
    today = datetime.datetime.now()
    year = today.year - birth_date.year
    month = today.month - birth_date.month
    day = today.day - birth_date.day
    if month > 0:
        age = year
    elif month < 0:
        age =year-1
    else:
        if day >= 0 :
            age = year
        elif day < 0:
            age = year-1
    print(age)

except Exception:
    print('WRONG')
