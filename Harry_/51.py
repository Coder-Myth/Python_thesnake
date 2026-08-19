# seek(): this function directly jumps to the given byte leaving then reads the other bytes

a = open("sample2.txt", "r")

p = a.seek(5)  # jumps 5 charecters forward

print(a.read(4))  # this will read 4 charecters forward of the given text

# tell(): this function tells from where is reading going to start
k = a.tell()  # this will return 5 as output

# truncate(): with the help of this you can directly fix the size of the file even more charecters are there written or appended

l = open("klo.txt", "w")
o = l.write("Hello World!")
l.truncate(5) #this directly only pics 5 charecters they are hello 
