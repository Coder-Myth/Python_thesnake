# f-strings: method to add variable in print stattements

# in old days
a = "Hello My Name {}, I'm from {}"

name = "Dhananjay"
country = "India"

print(a.format(name, country))  # or use index in the place of writing variable names

b = "Hello My Name {1}, I'm from {0}"

print(b.format(country, name))

# now the concept of f-string:
print(f"my name is {name}, I'm from {country}")

print(f"my name is {{name}}, I'm from {{country}}")
# output : my name is {name, I'm from{country}}


# <----------------------------------- concept in dictionary further------------------------------------>
# in f strings you can use this as : 

for key , value in range():
    print(f"Roll Number :{key}, \n marks: {value}")

    # using two variable in string