# class methods: a method that allows you to change the class i.e. not instance variable the class variable
# instance only changes the details for specific employee but class method allows you to change the class variable


class employee:
    retirement_age = 60

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def retire_age(self, retire_age):
        return self.retire_age

    def details(self):
        print(
            f"The Employee {self.name}\nhe is {self.age} years old\nIN {self.retire_age} years he will get retired."
        )


E1 = employee("Raja", 43)
E1.details()
