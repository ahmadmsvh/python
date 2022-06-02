my_set = {1,2,3}
print(my_set)

my_set = {1,2.43,'A',('apple',1)}
print(my_set)

my_set = {1,2,3,2}
print(my_set)
print(len(my_set))


my_set = set([1,2,3])
print(my_set)

variable = {}
print(type(variable))
variable = set()
print(type(variable))

variable.add(5)
print(variable)

variable.update([1,2,3])
print(variable)

variable.update([(4,15),6,'we'],('e','r','t','w','dw'),)
print(variable)