# writing data into a file, this will create the write.txt file
f = open("write.txt", "w")
f.write("This is the first data written using write mode, before file creation")
f.close()

f = open("write.txt", "r")
content = f.read()
print(f"Reading data on write.txt:\n{content}")
f.close()


# adding new content to the same file will cause losing old data
with open("write.txt", "w") as f:
    f.write("This is the new data adding to the write.txt")

# reading new content
with open("write.txt", "r") as f:
    content = f.read()
    print(f"Reading new content from write.txt:\n{content}")

# Writing multiple lines to the file
with open("write.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    f.write("Line 4\n")

# reading the newly added multiple lines
with open("write.txt", "r") as f:
    content = f.read()
    print(f"reading newly added multiple lines:\n{content}")


# write multiple strings at once using the writelines
lines = [
    "This is the first line\n",
    "This is the second line\n",
    "This is the third line\n",
    "This is the last line\n",
]
with open("write.txt", "w") as f:
    f.writelines(lines)
with open("write.txt", "r") as f:
    content = f.read()
    print(f"Reading new lines added using writelines():\n{content}")


# writing numbers to a file, add str(), because files only accept strings
number = 1000
with open("numbers.txt", "w") as f:
    f.write(str(number))

with open("numbers.txt", "r") as f:
    content = f.read()
    print(f"Reading file after adding number:\n{content}")

with open("numbers.txt", "w") as file:
    for i in range(1, 6):
        file.write(f"{i}\n")

with open("numbers.txt", "r") as f:
    content = f.read()
    print(f"Reading file number.txt:\n{content}")
