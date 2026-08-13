# manipulating list:

list = [1,2,3,4,5,6,7]

print(list)

list.append(7)  # add new elements

list.sort()  # sort the elements ascending order

list.sort(reverse=True)  # ----
#                          #   |---> sort list elements in descending order
list.reverse()  # - ------------

list.index(5)  # index starts fom zero and moves to the 5 and give its output

list.count("#value")  # count the times value inseted comes in it

list.pop(7) #removes 7 from list
 
list.insert("INDEX", "VALUE")  # inserts the value on the index given below

list.extend("VALUE1", "VALUE2")  # adds multiple value to the list

print(list)


list.copy()#this has got a catch in the list

m= list
m[0]=69

print(list)#expected output [1,2,3,4,5] but it comes out to be [69,2,3,4,5]

# i.e. we use list.copy()

# this creates a new list withthe same number of elements in list and now the new changes are there till the new list only 


#concatenate tuple: i.e. simply add two tuple in the output you will get the total no. of elements of both in new elements

# k(tuple1)--------
#                 |
#                 |-->l=k+g------> l=new tuple (l has all the elements there in k and g )
#                 |
# g(tuple2)--------
