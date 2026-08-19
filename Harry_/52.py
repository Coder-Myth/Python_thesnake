# lamda function : this is a way to create mini function in you program


def sum(a, b):
    return a + b


# this function can be also written as
double = lambda x: x * 2
# name = lambda arguments : operations/Expressions

cube = lambda y: y**3
print(cube(3))

 
# this is mostly used when lambda function is passed as an arguments example


def final_output(fx, v):  # here fx keyword is for function
