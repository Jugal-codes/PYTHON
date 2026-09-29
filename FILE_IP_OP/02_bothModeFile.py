# Mode 1 : r+ (Read + Write)
# Opens the file for both reading and writing. The file must already exist. 
# The cursor starts at the beginning, and writing will overwrite existing content.

# data.txt contains: "Hello World"

f = open("Basic_of_Python/FILE_IP_OP/data.txt", "r+")
print("Before:", f.read())   # Reads existing content

f.seek(0)                    # Move cursor to start
# f.seek(0,2)                # 0 offset, 2 means "end of file"   
f.write("Hi")                # Overwrites first 2 characters
f.close()




# Mode 2 : w+ (Write + Read)
# Opens the file for writing and reading. If the file exists, its content is erased. 
# If it doesn’t exist, a new file is created.

f = open("Basic_of_Python/FILE_IP_OP/data2.txt", "w+")
f.write("Python File I/O Exampleeeeeeeeeee")
f.seek(0)                    # Move cursor to start
print("After write:", f.read())
f.close()



# Mode 3 :a+ (Append + Read)
# Opens the file for appending and reading. If the file exists, new content is added at the end.
# If it doesn’t exist, a new file is created. Old content is preserved.

f = open("Basic_of_Python/FILE_IP_OP/data.txt", "a+")
f.write("\nNew line added")   # Always adds at the end
f.seek(0)                     # Move cursor to start
print("Full content:\n", f.read())
f.close()



