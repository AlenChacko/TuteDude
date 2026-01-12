import pickle


# Pickling a sample object
data = [10, 20, 30]

# always use "wb" mode , bacause pickle store bynary
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)


# Unpickling the object
with open("data.pkl", "rb") as file:
    data = pickle.load(file)
print(f"Reading data: \n{data}")


# pickle exception handling
try:
    with open("data.pkl", "rb") as file:
        data = pickle.load(file)
        print(data)

except FileNotFoundError:
    print("File not found")

except EOFError:
    print("File is empty")

except pickle.UnpicklingError:
    print("File is corrupted or invalid")

except Exception as e:
    print("Unexpected error:", e)


# using dumps() object to bytes (no file)
data = {"x": 100}
binary = pickle.dumps(data)
print(type(binary))  # bytes


# using loads() bytes to object
original = pickle.loads(binary)
print(original)
