# Map Filter Reduce
#map : 

cube = lambda x:x**3 
 
lst=[1,2,3,4,5,6]

c=list(map(cube ,lst))#
print(c)

# filter : this simply filter the element according to the required conditions

def required_value(k):
    return k>2

d=list((filter(required_value , lst)))
print(d)


#  reduce :
# 1. we need to import reduce this is not built in 
# this may be  used in libraries  like numpy pandas 
from functools import reduce

list=[1,2,3]

# syntax : variable_name = reduce(lambda arguments : operations)

c = reduce(lambda x,y: (x*y) , list)+10
print(c)

# mostly we use this in numpy 
