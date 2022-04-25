
class Class():

    def __init__(self,class_name):
        self.class_name = class_name
        self.class_pop = int(input())
        self.student_list = []
        self.number_of_students = len(self.student_list)
        
    def get_average_weight(self):
        sum = 0
        for student in self.student_list:
            sum += int(student.weight)
        weight_avg = sum/len(self.student_list)
        return weight_avg

    def get_average_height(self):
        sum = 0
        for student in self.student_list:
            sum += int(student.height)
        height_avg = sum/len(self.student_list)
        return height_avg

    def get_average_age(self):
        sum = 0
        for student in self.student_list:
            sum += int(student.age)
        age_avg = sum/len(self.student_list)
        return age_avg

class Student():

    def __init__(self,age,weight,height,class_name):
        self.age = age
        self.weight = weight
        self.height = height
        self.class_name = class_name
        class_name.student_list.append(self)


A = Class("A")

age_list = str(input()).split(' ')
height_list = str(input()).split(' ')
weight_list = str(input()).split(' ')

for i in range(len(age_list)):
    Student(age_list[i],weight_list[i],height_list[i],A)

B = Class("B")

age_list = str(input()).split(' ')
height_list = str(input()).split(' ')
weight_list = str(input()).split(' ')

for i in range(len(age_list)):
    Student(age_list[i],weight_list[i],height_list[i],B)

print(A.get_average_age())
print(A.get_average_height())
print(A.get_average_weight())

print(B.get_average_age())
print(B.get_average_height())
print(B.get_average_weight())


if A.get_average_height() > B.get_average_height():
    print('A')
elif A.get_average_height() == B.get_average_height():
    if A.get_average_weight() < B.get_average_weight():
        print('A')
    elif A.get_average_weight() == B.get_average_weight():
        print('Same')
    else:
        print('B')
else:
    print('B')


