import os

# Checking file exist
file = "read.txt"
if os.path.exists(file):
    with open(file) as f:
        content = f.read()
        print(f"Reading content if file exist:\n{content}")
else:
    print("File not exist")


# handling FileNotFoundError on reading
try:
    with open("read.txt", "r") as f:
        content = f.read()
        print(f"reading if file found:\n{content}")
except FileNotFoundError as file_error:
    print(f"Error:{file_error}")


# handling error on writing
try:
    with open("numbers.txt", "w") as f:
        f.write("This is from where exceptions handled")
except IOError:
    print("Something went wrong")
