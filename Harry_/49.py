# file I/O :handling a file

# open a file  (1. txt method , 2.Binary Method) , read , write , append ,close the file  ==>  some manipulative commands

# open a file
a = open("sample2.txt", "r")  # if not written 'r' by default it is the same


# modes :
# read mode : this gives you content in terminal , if file do not exists throws error
read = a.read()
print(read)
a.close()

 
# write mode : this file allows you to write inside the file , if not exists this creates one file
#    <==========this mode just removes the earlier content and only keeps your new content===========>
c = open("sample.txt", "w")
c.write("Hello World!")
c.close()


# append(): this adds the content when ever required
d = open("sample.txt", "a")
d.write("Hello World!")
