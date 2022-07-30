class MyClass:
    def __init__(self, edate=None, fdate=''):
        self.d = fdate
        self.e = edate
        if edate:
            print('cunstructors', edate)
        
        else:
            print('default constructor')

m1 = MyClass('2022-July-29')
m2 = MyClass(fdate = 'salam')
print(m2.d)
print(m2.e)
