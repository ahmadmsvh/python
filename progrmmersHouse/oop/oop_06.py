class Point:
    def __init__(self, x, y):
        self.move(x,y)

    def move(self,x,y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0,0)


obj1 = Point(1,2)

print(obj1.x, obj1.y)