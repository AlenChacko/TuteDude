"""
read mode (r)
opens file for reading
file must exist
raise error if file not exist
"""

# This will read the entire file
f = open("read.txt", "r")
content = f.read()
print(f"Reading entire contents from read.txt :\n{content}")
f.close()


# This will read the file in characters
f = open("read.txt", "r")
content = f.read(5)
print(f"Reading contents in characters from read.txt:\n{content}")
f.close()


# This will read one line
f = open("read.txt", "r")
content = f.readline()
print(f"Reading one line from read.txt:\n{content}")
f.close()


# This will read all lines as a list
f = open("read.txt", "r")
content = f.readlines()
print(f"Reading contents as a list:\n{content}")
f.close()


# Looping through a file
f = open("read.txt", "r")
print(f"Looping through read.txt:\n")
for line in f:
    print(line.strip())
f.close()


# Using with statement
# This will automatically close files
with open("read.txt", "r") as f:
    content = f.read()
    print(f"Reading contents using with method:\n{content}")


# reading large files in better way
with open("read.txt", "r") as f:
    for line in f:
        print(line)
