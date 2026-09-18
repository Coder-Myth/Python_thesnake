# instance variable and class variable :

# instance variable: this is a variable for the specific object

# class variable : this is a variable for the whole class whenever this is defined remains same till the instance variable is given to the object


class student:
    school_name = "LWCS"

    def __init__(self, student_name, roll_number):
        self.student_name = student_name
        self.roll_number = roll_number

    def show_details(self):
        print(
            f"Roll Number {self.roll_number} named {self.student_name} studied from this our school {self.school_name} "
        )


s1 = student("Raja", 45)
s1.show_details()
# for s1 this uses class variable

s2 = student("Dhananjay", 38)
s2.school_name = "AITR"  # this is an instance variable
s2.show_details()
# for s2 this uses instance varaible i.e. it only changes for the student s2

s3 = student("Dhairya", 37)
s3.show_details()
# this again uses class variable i.e. school_name