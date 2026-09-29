# SuperKeyword : if the class inherited does not has a function of the same name
# then super keyword steps back to the earlier class i.e. from child to parent and then finds function and finally gives output
# super keyword 

class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def cout(self):
        print(f"Name : {self.name}\nAge : {self.age}\n\n--------------------------------------\n")


class programmer(employee):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang

    def cout(self):
        print(f"Name : {self.name}\nAge : {self.age}\nLanguage : {self.lang}\n\n--------------------------------------\n")


a = employee("raja", 56)
a.cout()

b = programmer("Dhairya", 56, "python")
b.cout()