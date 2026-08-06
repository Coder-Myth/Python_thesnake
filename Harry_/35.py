#for loop with else

# we can use else with for loop 

for i in range(5):
    print(i)

else:
    print("Sorry no i")

    #loop is completed till the end of the loop if loop breaks then only this balue is not printed


for i in range(6):
    print(i)
    if i==5:
        break

else :
    print("sorry ")