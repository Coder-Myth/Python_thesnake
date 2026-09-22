#dir , __dict__ , help()

# these are the 3 methods:

# dir method : this tells that how many number of function are there in python specific library

x= [1,2,3,4]
print(dir(x))
#this tells all the methods in there for the method x

# __dict__ : this method converts attributes into mapped dictionary
class employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def details(self):
        print(f"this {self.name}\nage:{self.age}")

E1 =employee("raja", 45)
E1.details()
print(E1.__dict__)#this converts the attributes into dictionary i.e. mapped 

# Help(): this basically helps you to understand the class in a a better way i.e. it indicates help
print(help(employee))