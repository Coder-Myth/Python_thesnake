# class methods as constructor:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def details(self):
        print(f"Name--->{self.name}\nAge--->{self.salary}")

# what if the input is given in single string but seperated by a - for this we create a list that has 
a = Employee("Raja", 18000)
a.details()