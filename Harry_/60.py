#  day 60 code with harry python

#getter : used to access the private or hidden variables that cannot be easily and directly accessed @property

# setter : allows you to change the private value as well check the new value entered
# @variable_name.setter i.e. private varable or argument


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
obj.book_price = 450
print(obj.book_price)
obj.info_book()


class bank_account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    def show_account(self):
        print(
            f"Account Number: {self.account_holder} has {self.balance} rupees in his account"
        )


obj2 = bank_account(4552658845, 45000)
obj2.balance = 40000
print(obj2._balance)  # getter called
obj2.show_account()
