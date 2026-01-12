try:
    with open("create.txt", "x") as f:
        f.write("This is created using the create mode")
except FileExistsError as file_error:
    print(f"Error:{file_error}")
with open("create.txt", "r") as f:
    content = f.read()
    print(f"Reading data from create.txt:\n{content}")
