class book:
    def __init__(self, name, price, copy):
        self.book_name = name
        self._book_price = price# <---protected ---> but can be easily accessed i.e. more detail in getter and setter
        self.__book_copy = copy  # <---kept private --->

    def book(self):
        print(f" the book {self.book_name} is of {self.book_price} rupees.")


book1 = book("raja", 55, 18)
book1.book()
print(book1.book_name)  # this cannot be accessed


# to access the private variable we use mangling method in python
print(book1._book__book_copy)  # first access the private