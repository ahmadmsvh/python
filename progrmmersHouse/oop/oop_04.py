import math

class Point:
    def move(self,x,y):
        self.x = x
        self.y = y
    
    def reset(self):
        # self.x = 0
        # self.y = 0
        self.move(0,0)

    def calculateDistance(self,other_point):
        distance = math.sqrt((self.x-other_point.x)**2 + (self.y - other_point.y)**2)
        return distance

#------------Main-----------   

obj_haghdoust = Point()
obj_haghdoust.move(10,10)


obj_salimi = Point()
obj_salimi.move(20,20)


distance = obj_salimi.calculateDistance(obj_haghdoust)
distance = obj_haghdoust.calculateDistance(obj_salimi)
print(distance)