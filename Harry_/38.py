# raise error : whenever required error to be there as a custom

a = int(input("Enter Your Number that should be less that 10:"))

if a >= 10:
    raise ValueError("Invalid input \n Enter Your Number Below 10")

b = input("Number b/w 5&9:")
if b == "quit":
    print("Yeahhh")
elif not b.isdigit():
    raise ValueError("Not An Integer")
else:
    b=int(b)
    if (b > 5) and (b < 9):
        print(b)
    else:
        raise ValueError
