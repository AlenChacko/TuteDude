# adding first line
with open("append.txt", "a") as f:
    f.write("This is the firstline adding to the append.txt file\n")


# adding next line

with open("append.txt", "a") as f:
    f.write("This is the secondline adding to the append.txt file\n")

# reading file
with open("append.txt", "r") as f:
    content = f.read()
    print(f"Reading contents from append.txt:\n{content}")


# appending multiple lines
lines = [
    "My name is Alen\n",
    "I'm a 26 year old male\n",
    "Suffering from unemployment\n",
]

with open("append.txt", "a") as f:
    f.writelines(lines)

with open("append.txt", "r") as f:
    content = f.read()
    print(f"Printing after adding multiple lines:\n{content}")
