class Circle:
    def __init__(self, x=1, y=1, r=1):
        pass
    
        self.x = x
        self.y = y 
        self.r = r

    pi = 3.14159

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        if x < 1:
            self.__x = 1
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        if y < 1:
            self.__y = 1
        else:
            self.__y = y

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self,r):
        if r < 1:
            self.__r = 1
        else:
            self.__r = r
    
    def cir(self):
        return (2 * self.__r * Circle.pi)

    def surface(self):
        return (self.__r ** 2 * Circle.pi)

    def diameter(self):
        return (self.__r * 2)

    def draw(self):
        print(f'drew a circle with radius {self.__r} | {self.__x} | {self.__y}')


    
c1 = Circle()
c1.draw()
print(c1.surface())

c2 = Circle(12)
c2.draw()
print(c2.surface())


c3 = Circle(12, 13)
c3.draw()
print(c3.surface())


c4 = Circle(12, 13, 2)
c4.draw()
print(c4.surface())

c5 = Circle(r=10)
c5.draw()
print(c5.surface())