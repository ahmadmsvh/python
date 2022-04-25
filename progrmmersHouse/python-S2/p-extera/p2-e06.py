print("enter four name for candidates:")
first_name=input("enter the first name:")
second_name=input("enter the second name:")
third_name=input("enter the third name:")
forth_name=input("enter the forth name:")

minimum=first_name
if second_name<minimum:
    minimum=second_name;
if third_name<minimum:
    minimum=third_name
if forth_name<minimum:
    minimum=forth_name

print("the first name in alphabetic order is %s"%minimum)
    

