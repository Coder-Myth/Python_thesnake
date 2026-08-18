a = 5

def hello():
    a=6#local variable 
    print(a)


hello()
print(a)

def new():
    #modify global variable
    global a #global variable changed
    a=10
    return a


print(new())#
