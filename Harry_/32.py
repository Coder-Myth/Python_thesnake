# Methods in sets 

s1={1,2,3,4,7}
s2={4,5,6}
#--------------------------------------BASIC METHODS----------------------------------------------
# union : contains all the elements  of both sets

union =s1.union(s2)

update = s1.update(s2)# now s1 set contains all the value there in both set


print(union)

s3={1,2,3,4,57}
intersection =s3.intersection(s2)

print(intersection)

intersection_update= s2.intersection_update(s1)
# print(intersection_update)-----> output none because same elements that is the proof btw if you think it in a way
 

# symmetric_difference : values that are not common in the sets <-----values of both sets come-------->
symmetric_difference =s1.symmetric_difference(s2)
symmetric_difference_update =s1.symmetric_difference_update(s2)

# difference : removes the common elements from the dominating set and gives other elements
difference =s1.difference(s2)
 
