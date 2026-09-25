# class methods as constructor:
        print(f"Name--->{self.name}\nAge--->{self.salary}")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        # Split the string and unpack into name and salary
        name, salary = string.split("-")
        return cls(name, int(salary)) # Convert salary to int and pass as separate arguments
        
    def details(self):
        print(f"Name--->{self.name}\nSalary--->{self.salary}")

# what if the input is given in single string but  a - for this we create a list that has the words seperatedb= Employee() by -
# using class methods as a constructors
a = Employee("Raja", 18000)
a.details()

string = "Raj-120000"
b = Employee.fromStr(string)
b.details()