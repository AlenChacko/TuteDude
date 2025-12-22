# 12. Raw string / escape sequences
# print("C:'\'new_folder'\'test.txt")
# show me the answer

# 13.Multiple inputs in one line
a = 1
b = 2
c = 3
print(a * b * c)

# 14. Read until newline & count chars
text = "malayalam"
print(len(text))

# 15.Boolean input
inpt = "a"
res = bool(a)
print(res)

# 16. Literals & Keywords
print(type(123))
print(type(12.34))
print(type("Hello"))
print(type(True))

# 17.Forbidden keyword name
# if=5
# syntax error: if is a  reserved predefined keyword that has a meaning

# 18. Count keywords
import keyword

print(len(keyword.kwlist))

# 19. Use a keyword correctly
isStudent = True
if isStudent:
    print("Student")
else:
    print("Not student")

status = False
if status or 1:
    print("Done")

if True and True:
    print("True")


# 20. Numeric literal forms
# show me the answer
