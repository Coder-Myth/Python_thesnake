# pizza


class pizza:
    def __init__(self, size, topping):
        print("<<Welcome to Our Restaurant>>\t\n")
        self.size = input(
            "Size of Pizza:\n1 ===> Small\n2 ===> Medium\n3 ===> Large"
        )

    def size_of_pizza(self):
        self.size = int(self.size)
        if self.size == 1:
            return "Small"
        elif self.size == 2:
            return "Medium"
        elif self.size == 3:
            return "Large"

        topping = []
        while True:
            self.topping_on_pizza = input(
                "Among The Topping You Would Like To Have:\t\nClick 1 for Tomato\nClick 2 for Capsicum\nClick 3 for sauce\nClick 4 for Mayonise\nClick 5 to Exit and bill"
            )
            self.topping_on_pizza = int(self.topping_on_pizza)
            if self.topping_on_pizza == 1:
                return "Tomato"
            elif self.topping_on_pizza == 2:
                return "Capsicum"
            elif self.topping_on_pizza == 3:
                return "Sauce"
            elif self.topping_on_pizza == 4:
                return "Mayonise"
            self.topping_on_pizza.append(topping)

    def describe(self):
        print(
            f"Your Pizza is {self.size_of_pizza} and it has {self.topping_on_pizza} toppings on the pizza"
        )



p1 = pizza(None, None)
p1.size_of_pizza() 

p1.add_toppings()
