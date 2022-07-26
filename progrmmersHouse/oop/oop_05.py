class Circle:
    def __init__(self):
        self.r = 2
        self.x = 10
        self.y = 10
        self.color = 'red'
    
    def area(self):
        return ((self.r ** 2) * 3.14)

    def perimiter(self):
        return ((self.diameter()) * 3.14)

    def diameter(self):
        return(self.r * 2)

    def distance(self):
        return((self.x**2 + self.y**2)**0.5)

    def changeColor(self, new_color):
        self.color = new_color
    
c1 = Circle()

print(c1.color)
print(c1.area())
print(c1.perimiter())
print(c1.diameter())


c2 = Circle()

print(c2.distance())

c2.x = 20
c2.y = 20
c2.color = 'pink'


print(c2.color)
print(c2.area())
print(c2.perimiter())
print(c2.diameter())

c2.changeColor('green')

print(c2.color)

print(c2.distance())
