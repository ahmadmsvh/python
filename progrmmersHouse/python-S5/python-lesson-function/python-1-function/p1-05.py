#-------------------------<< Volume Of Cube >>-------------------------
def cubeVolume():
    s1 = enterNumber()
    s2 = enterNumber()
    s3 = enterNumber()
    vol = s1 * s2 * s3
    return vol
#-------------------------<< Get Number >>-------------------------
def enterNumber():
    num = int(input("enter a number:\t"))
    return num
#-------------------------<< Main Program >>-------------------------
volume = cubeVolume()
print(volume)