# class and objects


class info:  # class Blueprint
    name = "Enter Your Name:\n"
    Class = "Enter YOur Class:\n"
    Branch = "Enter Your Branch\n"

    def Details(self):
        print(
            f"{self.name} is in {self.Class} Class\nGoing to pursue {self.Branch} branch\n"
        )


a = info()  # object in python one or as per need i.e. object1
a.name = "Raja"
a.Class = "12th"
a.Branch = "cse"
a.Details() 


b = info()#object 2 
b.name = "Dhairya"
b.Class = "12th" 
b.Branch = "Aiml" 
b.Details()
