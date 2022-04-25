from array import array

#---------------<< Print Star >>---------------
def printStar(number):
    for i in range(0,number):
        print("*" , end = "")
    print("", end = "\n")


#---------------<< Main Program >>---------------
number = int(input("enter number of stars:\t"))

printStar(number)