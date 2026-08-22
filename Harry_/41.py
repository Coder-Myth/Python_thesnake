#short hand if else:
#must use this for only short singlt hand statements  not for more than one statement 

a= 45
b=884

print("A") if a>b else print("Equal") if a==b else print("B")
# <---1--><-2---><------------3-------------><------4------>

# 1==> statement to be excecuted 2==> if + condition behind it 3==>else + statement + if + condition

# also can be used a sa conditionals 

# <--------------------------------------------------------------------------------------------------------------> 
# use this as conditional statements
c="fuck" if a<b else ""# double quote returns nothing 
# if == true ----> c is printed and if not else statement is printed 

print(c)
# <--------------------------------------------------------------------------------------------------------------> 
# Question: Write a Python program that checks if a number is positive, negative, or zero using the shorthand if-else
# (ternary operator). Store the result in a variable called result and print it.

num = int(input("Enter Your Number:"))

# result = if num>0 print("Positive") else (num==0) print("Zero") else print("negative")
# print(result)

result = print("positive") if num>0 else print("Zero") if num==0 else print("Negative ")
print(result)