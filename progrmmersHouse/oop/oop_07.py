class Circle:
    def __init__(self):
        self.__x = 1
        self.__y = 1
        self.__r = 1

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
c1.x = 2
c1.y = 2
c1.r = 2

print(c1.cir())
print(c1.surface())
print(c1.diameter())
c1.draw()






