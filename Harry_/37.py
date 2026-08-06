# finally keyowrd : a program that is always excecuted

try:
    a = int(input("Enter Your Number:"))
except:
    print("Invalid Input")

finally:
    print("Your Desired Output")

 
print(
    "Your desired output"
)  # this is also always printed except when this is in function and function works as a return statement


# finally is always excecuted
def random_print():
    try:
        a = int(input("Enter Your Number:"))
        return 1
    except:
        print("Invalid Input")
        return 0
    finally:
        print("Your Desired Output") 
