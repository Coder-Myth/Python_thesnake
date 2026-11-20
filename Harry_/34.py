#  dictionary methods 

employee1={
    23:45,
    24:88

}

manager={
    25:55
}

employee1.update(manager)#update the dictionary

print(employee1)

manager.clear()#clear the dictionary

employee1.pop(24)#removes the selected key value
print(employee1)

employee1.popitem()#removes the last key value pair

print(employee1)

# del employee1 <-----deletes the dictionary------->


# --------------------------------------Input Methods-----------------------------------
# strip : to manage the spaces in the input string 

# Syntax : 
# var_nam.strip()

#find method : returns index of the element from where the given object starts, moves LEFT TO RIGHT 
#rfind method : returns index of the element from where the given object starts moves LEFT TO RIGHT

#syntax :
# var_name.find()
