# exception handling: handles the error and makes the further code run the same way as they should go with the flow


a= int(input("Enter Your Number:"))

for i in range(1,11):
    print(f"{a} X {i} = {a*i}")

  # if input in a is not an integer then this shows error 


try:
    n = int(input("Number:"))
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

except ValueError:
    print("Invalid Input")


except  IndexError:
    print("Index error")



 
'''
If the user enters something that's not a number (like "abc") → catch it and print "Please enter valid numbers."
If the user enters 0 as the second number (division by zero) → catch it and print "Cannot divide by zero."
If neither error occurs → print the division result.
'''

