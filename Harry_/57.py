# # class and objects


# class info:  # class Blueprint
#     name = "Enter Your Name:\n"
#     Class = "Enter YOur Class:\n"
#     Branch = "Enter Your Branch\n"

#     def Details(self):
#         print(
#             f"{self.name} is in {self.Class} Class\nGoing to pursue {self.Branch} branch\n"
#         )


# a = info()  # object in python one or as per need i.e. object1
# a.name = "Raja"
# a.Class = "12th"
# a.Branch = "cse"
# a.Details() 


# b = info()#object 2 
# b.name = "Dhairya"
# b.Class = "12th" 
# b.Branch = "Aiml" 
# b.Details()


class book():
    book_name="Enter Your Book Name:\n"
    book_author="Enter Your Book author:\n"
    book_price="Enter Your Book price:\n"

    def details_book(self):
        print(f"The \"{self.book_name}\" is written by {self.book_author},\nthe best book under {self.book_price}")

a =book()
a.book_name="venice"
a.book_author="shakespeare"
a.book_price="400 /-"
 
