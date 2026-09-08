#  constructor:  this is always called when there is an object created
#               this in terms helps to directly store value without giving varaible in different steps


# self is passed as an arguments
class person:
    def __init__(self, name, occupation):
        print("constructor Always called")
        self.name = name
        self.occupation = occupation

    def information(self):
        print(f"{self.name} is a fresher\nJoined as {self.occupation}")

b = person("Raja", "SDE")  # this store the value in name and occupation
# whenver the info is called then it prints the program
b.information()  # this prints the value given in string of function


# enhanced Code using constructor:
a = book()
a.book_name = "venice"
a.book_author = "shakespeare"
a.book_price = "400 /-"
a.details_book()


class book:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.book_author = author
        self.book_price = price

    def retail_book(self):
        print(
            f"The {self.book_name} written by { self.book_author} is best under {self.book_price}"
        )

c = book("Venice ", "Shake", "550/-")
c.retail_book()


# q2

class student:
    def __init__(self, name, roll_number, marks):
        self.student_name = name
        self.student_roll_number = roll_number
        self.student_marks = marks

    def student_details(self):
        print(
            f"Roll Number {self.student_roll_number} named {self.student_name} is awarded with {self.student_marks} marks."
        )

d= student("raja", 38, 76)
d.student_details()