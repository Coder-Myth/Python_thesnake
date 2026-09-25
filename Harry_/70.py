# class methods as constructor:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls,string):
        
        pass
    def details(self):
        print(f"Name--->{self.name}\nAge--->{self.salary}")


# what if the input is given in single string but  a - for this we create a list that has the words seperatedb= Employee() by -
# using class methods as a constructors
a = Employee("Raja", 18000)
a.details()


string = "Raj-120000"
b = Employee.fromStr(string)
b.details()