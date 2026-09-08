# Decorators:
# this function basically takes the function under @decorator as input and perform the other tasks


def price_alltoment(fx):
    def price_loading():
        print("price loading........\n")
        fx()
        print("Price Displayed")

    return price_loading


@price_alltoment
class book:
    def __init__(self, book_name, book_price, book_author):
        self.book_name = book_name
        self.book_price = book_price
        self.book_author = book_author

    def info_books(self):
        print(
            f" the book {self.book_name} written by {self.book_author} is best under {self.book_price}"
        )


book12 = book("venice ", 550, "shakespeare")
book12.info_books()