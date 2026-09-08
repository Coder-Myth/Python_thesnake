#  day 60 code with harry python
# getters and setters :
# the @property is the getter
# setter sets the value


class book:
    def __init__(self, book_name, book_price):
        self.book_name = book_name
        self._book_price = book_price

    @property
    def book_price(self):
        return self._book_price

    @book_price.setter
    def book_price(self, new_price):
        self._book_price = new_price

    def info_book(self):
        print(f"The book {self.book_name} is of {self.book_price} rupees.")


obj = book("raj", 550)
obj.book_price =450
print(obj.book_price)
obj.info_book()