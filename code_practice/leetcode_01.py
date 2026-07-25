Number_of_elements = int(input("Number of Elements:"))
num = []

for i in range(0, Number_of_elements):
    i = int(input())
    num.append(i)

print(num)

Target_start=int(input("Starting Index:"))
Target_end=int(input("Ending Index:"))


for j in range(Target_start, Target_end+1):
    Sum_of_Array=0
    Sum_of_Array += num[j]
#    Sum_of_Array = Sum_of_Array + num[j]


print(Sum_of_Array)

