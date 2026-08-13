# recursion:  calling function in same function with different arguments

# find sum of n numbers

def sum(n):
    if n==1: #base case return this when value is about to end
        return 1
    else:
        return sum(n-1)+n

# sum(4)
print(sum(4))

# same goes for factorial

def factorial(m):
    if m==0 or m==1:
        return 1
    else :
        return factorial(m-1)*m

print(factorial(5))

# print n numbers

def print_numbers(n):
    if n==0:
        return # base cap does not further recurse the function 
    else:
        print(n)
        return print_numbers(n-1)

print(print_numbers(4))

print("end\n")

#<------------------------sum of digits:(1234-->1+2+3+4)------------------------>

# number--> string --> slicing --> integer--> Add

# # sum=[]

# def sum_of_digit_2(n):
#     sum=[]
#     string=str(n)
#     for i in string:
#         # print(i)
#         integer =int(i)
#         # print(type(integer))
#         sum.append(integer)
#     return sum(sum)
# #
# # print(sum)
# # print(sum_of_digit_2(8456))
# sum_of_digit_2(8456)

#fibbonacci series:(0,1,1,2,3,5,8......) 

def fib_series(n):
    # print(1)
    if n==0 or n==1:
        return 1
    else:
        # print(fib_series(n-2)+fib_series(n-1))
        return fib_series(n-2)+fib_series(n-1)
n=19
for i in range(1,n+1):
    print(fib_series(i) , end =" ")
