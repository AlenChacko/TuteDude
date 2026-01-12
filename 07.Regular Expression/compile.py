"""
====================================================
REGEX COMPILE FUNCTION IN PYTHON (re.compile)
====================================================

This file explains:
- What re.compile() is
- Why we use it
- How it works internally
- Using flags
- Reusing compiled patterns
- Real-world examples

Audience: Beginners
"""

import re


print("\n===================================")
print("1. WHAT IS re.compile()?")
print("===================================")

# re.compile() converts a regex pattern into a
# REGEX OBJECT that can be reused multiple times

pattern = re.compile(r"\d+")
text = "Order 123, Item 456"

result = pattern.findall(text)
print("Text:", text)
print("Matches:", result)

# Explanation:
# Instead of writing re.findall(pattern, text)
# we create a pattern object and reuse it


print("\n===================================")
print("2. WITHOUT compile() vs WITH compile()")
print("===================================")

text = "Apple 10 Banana 20"

# Without compile
result1 = re.findall(r"\d+", text)

# With compile
compiled_pattern = re.compile(r"\d+")
result2 = compiled_pattern.findall(text)

print("Without compile():", result1)
print("With compile()   :", result2)

# Explanation:
# Output is SAME
# compile() is better when pattern is reused


print("\n===================================")
print("3. REUSING COMPILED PATTERN")
print("===================================")

pattern = re.compile(r"\b\w{4}\b")

texts = ["This is a test", "Python code here", "Find four word size"]

for t in texts:
    print("Text:", t)
    print("Matches:", pattern.findall(t))
    print("-----")

# Explanation:
# Pattern is compiled once
# Used multiple times efficiently


print("\n===================================")
print("4. USING METHODS OF COMPILED OBJECT")
print("===================================")

text = "Email: test123@gmail.com"

pattern = re.compile(r"\w+@\w+\.\w+")

print("search():", pattern.search(text).group())
print("findall():", pattern.findall(text))
print("finditer():")

for match in pattern.finditer(text):
    print(match.group(), "at", match.span())

# Explanation:
# Compiled pattern has same methods as re module:
# search, match, findall, finditer, sub, subn


print("\n===================================")
print("5. SUBSTITUTION USING COMPILED PATTERN")
print("===================================")

text = "My number is 9876543210"
pattern = re.compile(r"\d")

result = pattern.sub("X", text)
print("Text:", text)
print("Result:", result)

# Explanation:
# sub() can be called on compiled pattern


print("\n===================================")
print("6. USING FLAGS WITH compile()")
print("===================================")

text = "python PYTHON Python"

pattern = re.compile(r"python", re.IGNORECASE)
result = pattern.findall(text)

print("Text:", text)
print("Matches:", result)

# Explanation:
# IGNORECASE → matches all case variations


print("\n===================================")
print("7. MULTIPLE FLAGS")
print("===================================")

text = "Hello\nPython\nWorld"

pattern = re.compile(r"^Python", re.MULTILINE)
result = pattern.findall(text)

print("Text:", repr(text))
print("Matches:", result)

# Explanation:
# MULTILINE → ^ and $ work on every line


print("\n===================================")
print("8. DOTALL FLAG")
print("===================================")

text = "Start\nMiddle\nEnd"
pattern = re.compile(r"Start.*End", re.DOTALL)

result = pattern.search(text)
print("Text:", repr(text))
print("Match:", result.group())

# Explanation:
# DOTALL → '.' matches newline too


print("\n===================================")
print("9. COMBINING FLAGS")
print("===================================")

pattern = re.compile(r"python", re.IGNORECASE | re.MULTILINE)

text = "Python\npython\nPYTHON"
result = pattern.findall(text)

print("Text:", repr(text))
print("Matches:", result)

# Explanation:
# Flags are combined using | (OR)


print("\n===================================")
print("10. REAL-WORLD EXAMPLE: PASSWORD CHECK")
print("===================================")

password_pattern = re.compile(r"^(?=.*[A-Z])(?=.*\d).{8,}$")

passwords = ["Pass1234", "password", "Short1"]

for pwd in passwords:
    if password_pattern.match(pwd):
        print(pwd, "→ Valid")
    else:
        print(pwd, "→ Invalid")

# Explanation:
# At least one uppercase letter
# At least one digit
# Minimum 8 characters


print("\n===================================")
print("SUMMARY")
print("===================================")

print(
    """
re.compile()
- Compiles regex into object
- Improves readability
- Improves performance when reused
- Supports all regex methods
- Supports flags

Common Flags:
IGNORECASE
MULTILINE
DOTALL
VERBOSE
"""
)

print("\n==============================")
print("END OF COMPILE DEMO")
print("==============================")
