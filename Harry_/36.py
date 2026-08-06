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
 
