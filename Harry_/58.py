#  constructor:  this is always called when there is an object created 
#               this in terms helps to directly store value without giving varaible in different steps 

#self is passed as an arguments
class person:
    def __init__(self,name , occupation):
        print("constructor Always called")
        self.name=name
        self.occupation=occupation
    def information(self):
        print(f"{self.name} is a fresher\nJoined as {self.occupation}")
 
a= person("Raja", "SDE")#this store the value in name and occupation
# whenver the info is called then it prints the program

a.information()#this prints the value given in string of function 
