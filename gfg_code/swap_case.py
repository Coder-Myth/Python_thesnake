#day 1 

#swap case 

a="GeeksForGeeks"

b=" HEllo"
#third variable  logic 
c=a
a=b
b=c

print(a ,b )

# Comma Assignmenmt Method
a,b= b,a

print (a)
print (b)


#print a times a and b times b and in between them add a symbol that is @

a=input(":")
b=input(":")

print(a*int(a), b*int(b), sep="@")