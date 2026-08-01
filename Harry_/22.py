# data type

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Harry", True]
print(list)

# list : changeable,  ordered , store multiple item in single variable

# index : accessing different items from list /

# negative indexing ---> positive indexing  len(name)-x
 # data type

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, "Harry", True]
print(list)

# list : changeable,  ordered , store multiple item in single variable

# index : accessing different items from list /

# negative indexing ---> positive indexing  len(name)-x

# check something in python

if 4 in list:
    print("Yes")
else:
    print("No") 


# Jump INdex

# print(list[start:end:jump])

print(list[1:: 3])# [2,5,8,true]jump is skip 1 skip 2 now give three 

print(list[1:])#till end 
print(list[1:4])#till 4 not including 4th index
print(list[1:-1])#negative indexing 

#<---------------- list comprehension ---------------------------->
# on the fly generating a list 

# there was no list before but as i got need i  just started making list 

# there was no list before but as i got need i  just started making list 

 
lst = [i for i in range(9)]
#     |---||----------------|   
#     |var |       loop     |
 
