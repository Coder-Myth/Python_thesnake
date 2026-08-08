# dictionary: ordered key value pairs 

dict= {
    "raja":12,#"raja"-----> key, 12----> value
    "dh":43,
    "ttt":4332
}
print(dict["dh"])
#loop to access or selected value using range function
for i in dict:
    print(dict[i])

print(dict.items())


# in f strings you can use this as : 

for key , value in dict.items(): 

    print(f"Name :{key}, \nmarks: {value}")

# using two variable in f string via dictionary defined
