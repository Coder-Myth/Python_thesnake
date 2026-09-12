# pizza


class pizza:
    def __init__(self, size, topping):
        print("<<Welcome to Our Restaurant>>\t\n")
        self.size = input("Size of Pizza:\n1 ===> Small\n2 ===> Medium\n3 ===> Large")
        self.topping = []

    def size_of_pizza(self, size_of_pizza):
        self.size_of_pizza = int(self.size)
        if self.size_of_pizza == 1:
            self.size_of_pizza == "Small"
        elif self.size_of_pizza == 2:
            self.size_of_pizza == "Medium"
        elif self.size_of_pizza == 3:
            self.size_of_pizza == "Large"

    def add_toppings(self):
        while True:
            self.topping_on_pizza = input(
                "Among The Topping You Would Like To Have:\t\nClick 1 for Tomato\nClick 2 for Capsicum\nClick 3 for sauce\nClick 4 for Mayonise\nClick 5 to Exit and bill"
            )
            self.topping_on_pizza = int(self.topping_on_pizza)
            if self.topping_on_pizza == 1:
                self.topping.append("Tomato")
            elif self.topping_on_pizza == 2:
                self.topping.append("Capsicum")
            elif self.topping_on_pizza == 3:
                self.topping.append("Sauce")
            elif self.topping_on_pizza == 4:
                self.topping.append("Mayonise")
            elif self.topping_on_pizza == 5:
                break

    def describe(self):
        print(
            f"Your Pizza is {self.size} and it has {self.add_toppings} toppings on the pizza"
        )


p1 = pizza(None, None)
p1.size_of_pizza()
p1.add_toppings()
p1.describe()
