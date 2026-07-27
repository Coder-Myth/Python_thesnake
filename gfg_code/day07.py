# function :instead of writing a long code again and again we just go with it and write a block of code giving it a name 
#lines of code gets less , code becomes more efficient 

#simple function 
def sum():
  print("Sum")

#argumented function :

def sum(a, b):
  sum=a+b
  print(sum)


#it gives a decent and approach in the coding 

#function and if else make condition that are getting worse and tough easier 
#i just keep doing practice this in a better way 


# Write a Python program to count the number of even and odd numbers in a list.
numbers = [12, 7, 5, 22, 9, 18, 3, 4]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
