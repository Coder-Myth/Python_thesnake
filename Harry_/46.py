#os module: helps you to create data folders, files , etc

# rename many files etc explore this on internet 

# and after you print the statement then you the folder is created 
import os 

#please don't run this code else folder named : 48-100 will be created 
for i in range(47,100):
    print(os.mkdir(f"data/{i}.py"))

