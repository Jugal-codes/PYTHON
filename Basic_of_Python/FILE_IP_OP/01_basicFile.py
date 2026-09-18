'''
The Random Access Memory(RAM) is volatile (data won't save),
and all its contents are lost once a program terminates in order.

To persist the data forever, we use files.
A file is stored in a storage device.
A python program can talk to the file by reading and writing content from it

There are 2 types of file:
    1. Text File
    2. Binary File

Syntax:
file.open("File_name","mode")
file.close()
'''

# Opening & Closing Files
# 'x' mode - Creates a new file.
# If the file already exists, it will throw an error (FileExistsError).
# Safer than w mode, because w will overwrite an existing file, but x will not.

# f = open("Basic_of_Python/FILE_IP_OP/newFile.txt", "x")
# f.close()

# read
# if file not exist -> gives FileNotFoundError
# file = open("Basic_of_Python/FILE_IP_OP/file404.txt")

# data = file.read()
# print(data)

# file.close()


# First create txt file - file1.txt
f = open("Basic_of_Python/FILE_IP_OP/file1.txt","r")

data = f.read()
print(data)

f.close()



# write 
# In write, if file not exist -> it will create
# If file exist then it'll overwrite the data 

f = open("Basic_of_Python/FILE_IP_OP/write.txt","w")
f.write("Namaste")
f.close()

# User enter's data
# f = open("Basic_of_Python/FILE_IP_OP/write2.txt", "w")
# text = input("Enter a text : ")
# f.write(text)
# f.close()

# We can create file any where using location
f = open("Basic_of_Python/write_anywhere.txt", "w")
f.write("Hello")
f.close()




# append 
# In append, add data without removing previous data
f = open("Basic_of_Python/FILE_IP_OP/file.txt", "a")
f.write("\nHELLOOOOOOOOOOOOO, GOODDDDDDDDDD MORNINGGGGGGGGGG!!")
f.close()





f = open("Basic_of_Python/FILE_IP_OP/file.txt", "r")
data = f.read()
data = f.read(4)

print(data)
f.close()