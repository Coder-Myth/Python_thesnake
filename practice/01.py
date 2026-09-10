# pizza


class pizza:
    def __init__(self, size, topings):
        print("<<Welcome to Our Restaurant>>\t\n")
        size_of_pizza = input(
            "Size of Pizza You Would Like To Have:\n CLick 1====> for the small\nCLick 2====> for the medium\nCLick 3====> for the large"
        )
        topping_on_pizza = input("Among The Topping You Would Like To Have:\t\n")

        def describe(self):
            print(
                f"Your Pizza is {size_of_pizza} and it has {topping_on_pizza} toppings on the pizza"
            )