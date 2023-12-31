"""
'r' : read only
'w' : write only
'a' : appending data at the end of file
'wt' : write text
'rt' : read text
'wb' : write binary
'rb' : read binary
"""
# f = open("name.txt")
# print(f.read())
# f.close()
# print(f.closed)

# f = open("name.txt", 'w')
# f.write("I am writable now")
# f.close()

## for avoicing f.close()
# with open("name.txt", "r") as f:
#     print(f.read())
# print(f.closed)

# with open("name.txt", "w") as f:
#     f.write("Hey I am good")


# with open("new.txt", "w") as f:
#     f.write("Hey new file is created")

# # WRite is existing file
# with open("new.txt", "w") as f:
#     f.write("This is the updated content of our file\n")
#     f.write("This is the updated content of our file")


# Reading the file

# with open("name.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("new.txt", "r") as f:
#     # Reading fist 4 characters
#     data = f.read(4)
#     print(data)

#     print(f.tell())
#     # next 10 characters
#     data = f.read(10)
#     print(data)

#     # Tells you the positoion of yuou r file handler
#     print(f.tell())

#     # Using seek you can reset your file handler
#     f.seek(2)
#     print(f.tell())


# # readliiness: reads line by line
# with open("new.txt", "r") as f:
#     data = f.readlines()
#     print(data)
#     for i in data:
#         print(i)