# str.py - Practical examples for strings

# Basic strings
s1 = 'Hello'
s2 = "World"
s3 = """This is
a multiline string"""
print("s1, s2:", s1, s2)
print("s3:", s3)

# Concatenation and repetition
print("Concatenate:", s1 + " " + s2)
print("Repeat:", s1 * 3)

# Indexing and slicing
msg = "Python"
print("msg[0]:", msg[0])
print("msg[-1]:", msg[-1])
print("msg[1:4]:", msg[1:4])

# f-strings and formatting
name = "Alen"
age = 21
print(f"My name is {name} and my age is {age}")
print("Old style: %s %d" % (name, age))
print("format:", "{} is {}".format(name, age))

# Escape sequences and raw strings
print("Newline:\nSecond line")
print(r"C:\Users\Alen\Desktop")

# Useful methods
text = "  Hello World  "
print("strip:", text.strip())
print("lower:", text.lower())
print("upper:", text.upper())
print("replace:", text.replace("World", "Python"))
print("split:", "a b c".split())
print("join:", ",".join(["a","b","c"]))

# Immutability demonstration
s = "abc"
print("id before:", id(s))
s = s + "d"
print("id after:", id(s))  # new object
