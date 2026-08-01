# function as arguments :

# default arguments :
# keyword arguments :
# required arguments :
# Variable length arguments :

# default arguments: if any of the argument is not assigned new vlue it already has a default value 

def Code(a=9, c=14):
    print(a+c)

Code(34 , 45)#a=9,b=14 ignored but 

Code(34)#a=34, b=14

Code(c=98)#a=9, b=98

#keywords Arguments : order doesnot matter if the given argument is in the way given below
Code(c=46, a=76)#keyword argument
 



#required arguments :

def Code2(a, b, c=45):
    print(a+b+c)

Code2(34,45) # here c is default argument but not a & b this are required arguments

# if not given required arg then error will be there shown


#return statement : value that is returned and stored whenever the function is called 

 
# we can use function argument as list tuple or dictionary

def sum(*numbers):# l=tuple
    pass


def sum(**numbers):# l=dictionary
    pass

