# Update a


# Step 2: Read file
with open("update.txt", "r") as f:
    content = f.read()
    print(f"Reading data before updating:\n{content}")

# Step 2: Modify content
content = content.replace("purpose", "feature")

# Step 3: Write back
with open("update.txt", "w") as f:
    f.write(content)

with open("update.txt", "r") as f:
    content = f.read()
    print(f"Reading data after updating:\n{content}")


print(
    "################################################################################################"
)

# Update a line
# Step 1: Read files line by line
with open("update.txt", "r") as f:
    content = f.readlines()
    print(f"Printing lines before update:\n{content}")

content[1] = "This line is updated now\n"

with open("update.txt", "w") as f:
    f.writelines(content)

with open("update.txt", "r") as f:
    content = f.read()
    print(f"Printing lines after update:\n{content}")
