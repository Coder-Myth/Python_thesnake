# inheritance: class====> modified class
# this simply converts class into a modified class


class student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def student_details(self):
        print(
            f"student named {self.name} whose roll number {self.roll_number} is a boy "
        )

obj = student("raj", 98)
obj.student_details()

# now new details branch has to be added 

class update1(student):
    def __init__(self, branch):
        self.branch=branch

    def student_details(self):
        print("Whose branch is Aiml")

obj = update1("Aiml")
obj.student_details()