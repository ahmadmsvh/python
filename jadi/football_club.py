import random 

class Person():
    
    def __init__(self,name):
        self.name = name

class Foothballist(Person):

    def __init__(self,club):
        self.club = club


names_list = ['Hossein','Mazyar','Akbar','Nima','Mehdi','Farhad','Mohammad',
                'Khashayar','Milad','Mostaf','Amin','Saeid','Puya','pourya',
                'Reza','Ali','Behzad','Soheil','Behrooz','Shahrooz','Saman',
                'Mohsen']

persons = []

for person in range(22):
    persons.append(Foothballist(''))

for person in persons:
    person.name = names_list[persons.index(person)]


A_counter = 0
B_counter = 0

for person in persons:
    rand_club = random.randint(0,1)
    if rand_club == 0:
        A_counter += 1
        if A_counter < 11:
            person.club = 'A'
        else:
            person.club = 'B'
    elif rand_club == 1:
        B_counter += 1
        if B_counter < 11:
            person.club = 'B'
        else:
            person.club = 'A'

for person in persons:
    print(person.name,person.club)
