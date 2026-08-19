# readlines method: this simply read the code line by line

# we have to use loop for this

a=open('sample2.txt', 'r')

while True:
    if not a.readline():
        break
    print(a.readline())

# another using variable
c=open.readlin()

while True:
    b=a.readline()
    if not b:
        break
    print(b)


# writeline()

f= open('sample2.txt', 'w')
lines=['hello\n', 'World\n', '!\n', "variable\n"]
f.writelines(lines)
f.close()

 