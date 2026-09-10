# library management system:
class library:

    def list_book(self):
        print("<<<<<The Books>>>>>")
        self.books = [
            "Python Crash Course",
            "Automate the Boring Stuff with Python",
            "The Pragmatic Programmer",
            "Clean Code",
            "Fluent Python",
            "Head First Python",
            "Effective Python",
            "Learning Python",
            "Think Python",
            "Python Cookbook",
        ]
        for i in range(0, len(self.books)):
            print(i, "===>", self.books[i])
        print("<<<<<These are the books>>>>>")

    books = []

    def add_book(self):
        pass

    def books_in_cart(self):

        for i in range(1, len(self.books)):
            if len(self.books) == 0:
                print("No Books in the cart\n")
            else:
                print(self.books[i])


lib = library()

while True:
    book_list = []
    user_status = int(
        input(
            (
                "1==> List all books\n 2==> Add Books\n3==> book in cart\n4==> bill and exit "
            )
        )
    )
    if user_status == 4:
        print("Thank You \n You May Reach The Counter\n")
        break
    elif user_status == 1:
        lib.list_book()
    elif user_status == 2:
        lib.add_book()
    elif user_status == 3:
        lib.books_in_cart()
    else:
        print("<<<INVALID INPUT>>>")
