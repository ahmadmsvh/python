class Car:
    def __init__(self, x = 0, y = 0, total_move = 10):
        self.x = x
        self.y = y
        self.total_move = total_move

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,x):
        if x < 0:
            self.__x = 0
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self,y):
        if y < 0:
            self.__y = 0
        else:
            self.__y = y
    
    @property
    def total_move(self):
        return self.__t
    @total_move.setter
    def total_move(self,total_move):
        if total_move < 0:
            self.__t = 0
        else:
            self.__t = total_move


    def right(self,r=1):
        if self.total_move > r:
            self.x += r
            self.total_move -= r
        else:
            print('out of move')

    def left(self,l=1):
        if self.total_move > l:
            self.x -= l
            self.total_move -= l
        else:
            print('out of move')

    def up(self,u=1):
        if self.total_move > u:
            self.y -= u
            self.total_move -= u
        else:
            print('out of move')

    def down(self, d=1):
        if self.total_move > d:
            self.y += d
            self.total_move -= d
        else:
            print('out of move')


car1 = Car(10,10,12)
car1.right(r = 3)
car1.right()
car1.down(d = 2)
car1.down()
car1.left()
car1.up()
car1.up()
car1.right()
car1.right()
car1.down()
car1.down()
car1.down()

print(car1.x,car1.y,car1.total_move)