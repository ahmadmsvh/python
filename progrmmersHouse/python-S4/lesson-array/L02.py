# def f(x):
#     x = x*2
    
# x = 5 
# f(x)
# print(x)


from array import array
def buildArray(length):
        
    array_name = array("i", [0] * length)
    a = array("", [array_name] * length)
    
    return a

arr = buildArray(10)
print(arr)