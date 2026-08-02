# tuples in python
# this is same as list but here the only change is it cannot be changed they are immutable


tuple = (1, 2, 3, 4, "apple", True)

# we can here print  len(tuple), negative indexing , string slicing , check **if 4 in tuple:**  , indexing

# here the thing that works is same as that of list i.e. tuple jump index or slicing but a catch that this may only work by creating a new tuple
tuple[1:4] 

res = tuple.index(3) #gives you first occurence of 3 in tuple

# but if we need to check in a given interval then 
 

res= tuple.count(3, 0,2) #count number of time 3 comes in interval

res=tuple.index(3,2,4) # (value, start , index )
 

res = len(tuple)#tells you length of tuple


tuple1 = tuple[1:4]
print(tuple)

#there are more thing  to add 
