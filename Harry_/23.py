# manipulating list:

list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]

print(list)

list.append(7)  # add new elements

list.sort()  # sort the elements ascending order

list.sort(reverse=True)  # ----
#                          #   |---> sort list elements in descending order
list.reverse()  # - ------------

list.index(5)  # index starts fom zero and moves to the 5 and give its output

list.count("#value")  # count the times value inseted comes in it

list.pop(7) #removes 7 from list
 
