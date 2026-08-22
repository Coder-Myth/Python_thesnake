# import 

# import takes all the built in function in python 
# import (name of library)
import math 

# another way to import only specifice library 
# from math import pi , sqrt 
# this installs only pi and sqrt function from math
from math import pi , sqrt 

# you can name the library when required to make it the way you want 
# import numpy as np ----> numpy is named as np 
# now everywhere you can use it as np not numpy
import math as m

# now use this name 
result = m.sqrt(9) #---> this gives 3 as output

# dir function

# this function tell or lists all the function in the library 
print(dir(math))

# we can import function or variable from the same program as well 
# just see go to video sample
# from sample import *
from sample import raja

# print(sample)
print(raja)# this is a function 
print(raja())# returns data type as well as name as print statement