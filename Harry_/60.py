#  day 60 code with harry python

# getter : used to access the private or hidden variables that cannot be easily and directly accessed @property

# setter : allows you to change the private value as well check the new value entered
# @variable_name.setter i.e. private varable or argument

# conditions for setter:
# 1. name of getter and function and the @mark_name.
# 2. setter should be the same hidden or protected variable should be the same.
# 3. else is the same process.


class book:
    def __init__(self, book_name, book_price):
        self.book_name = book_name
        self._book_price = book_price

    @property
    def book_price(self):
        return self._book_price

    @book_price.setter
    def new_book_price(self, new_price):
        self._book_price = new_price

    def info_book(self):
        print(f"The book {self.book_name} is of {self.book_price} rupees.")


obj = book("raj", 550)

# this is getter syntax : print(object_name.function_name[getter_function_name])
print(obj.book_price)  # this is getter

# this is setter syntax: object_name.functionname[setter_function_name] = new_value
obj.new_book_price = 450  # this sets price
obj.info_book()  # this calls function that sets the value and return the new value


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
