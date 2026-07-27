#flow Control :
#if , if -else, elif matchcase statements

a =int(input())

if(a>0):
    print("Positive")

elif(a==0):
    print("Zero")

else:
    print("Negative")


# match case statements
match a:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Invalid")

#you can practic three question they are :
# even odd , leap year , calculator , largest of three numbers 

a = int(input())

if a%2 == 0:
    print("Even")
else :
    print("Odd")

match a:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Invalid")

