# Decorators:
# this function basically takes the function under @decorator as input and perform the other tasks
# decorator basically helps function to be decorated in the class itself.

def price_alltoment(fx):
    def price_loading(*args, **kwargs):# *arguments, * keywordsarguments
        print("price loading........\n")
        fx(*args, **kwargs)
        print("Price Displayed")

    return price_loading

class book:
    def __init__(self, book_name, book_price, book_author):
        self.book_name = book_name
        self.book_price = book_price
        self.book_author = book_author

    # @price_alltoment
    def info_books(self):
        print(
            f"The book {self.book_name} written by {self.book_author} is best under {self.book_price}\n"
        )


price_allotment(info_sbook)()
book12 = book("venice ", 550, "shakespeare")
book12.info_books()