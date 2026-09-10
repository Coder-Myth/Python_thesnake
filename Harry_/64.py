# library management system:
class library:

    books = [
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

    def list_book(self):
        print("<<<<<The Books>>>>>")
        for i in range(0, len(self.books)):
            print(i, "===>", self.books[i])
        print("<<<<<These are the books>>>>>")

    cart_books = []

    def add_book(self):
        book_index_status = int(input("Enter Your book Index:\n"))
        for i in books:
            if book_index_status== i :
                print(books[i])
            else:
                continue
            pass
        # 1. first store the index  
        # 2. now go to the self.books 
        # 3. read the index and return in the book name from that index

        pass

    def books_in_cart(self):
            if len(self.cart_books) == 0:
                print("No Books in the cart\n")
            else:
                for i in range(0, len(self.cart_books)):
                    print(self.cart_books[i])

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
