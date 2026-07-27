'''st = {int(x) for x in input().split()}
i = int(input())
r = int(input())

########### Write your code below ###############
# Insert i in set

########### Write your code above ###############

# Printing the set
for i in sorted(st):
    print (i, end=' ')
print()

########### Write your code below ###############
# Remove r from set

########### Write your code above ###############

# Printing the set
for i in sorted(st):
    print (i, end=' ')
print()

########### Write your code below ###############
sum = # Sum of set elements
########### Write your code above ###############

# Print sum of set
print(sum) '''

#this is the code condition make the out as 
''' 
Input: st = [6, 7, 81, 2, 1], i = 3, r = 6
Output: 
1 2 3 6 7 81
1 2 3 7 81 
94
'''
# the same should be the output 

# this is what the solution looks like 

st = {int(x) for x in input().split()}
i = int(input())
r = int(input())

# Insert i in set
st.add(i)

# Printing the set
for i in sorted(st):
    print(i, end=' ')
print()

# Remove r from set
st.discard(r)

# Printing the set
for i in sorted(st):
    print(i, end=' ')
print()

s = sum(st)

# Print sum of set
print(s)
