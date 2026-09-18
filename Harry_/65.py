# static method : a method that works as a function that in class, it never requires self to be passed as an arguments


class add:
    def __init__(self, num):
        self.num = num

    def update(self, c):
        self.c = c
        return c + self.num


    @staticmethod
    def mean(a, b):
        return (a + b) / 2

    def new_number(self):
        print(f"The New Number is {self.hello}")


sum_1 = add(1)
final = sum_1.update(5)
print(final)
print(add.mean(4,5))# this is static method that can be directly called as well now requirement for the self .keyword