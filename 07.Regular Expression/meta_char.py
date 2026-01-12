"""
===========================================
REGULAR EXPRESSIONS (REGEX) DEMO IN PYTHON
===========================================

This file demonstrates the most important
regex symbols and how they work using
Python's built-in `re` module.

Audience: Beginners
"""

# Import the regex module
import re


print("\n==============================")
print("1. DOT (.) → Any single character")
print("==============================")

text = "cat bat rat"
pattern = r".at"

# findall() returns all matching patterns
result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# .  → any single character
# at → literal characters
# Matches: cat, bat, rat


print("\n==============================")
print("2. CARET (^) → Start of string")
print("==============================")

text = "Python is powerful"
pattern = r"^Python"

result = re.search(pattern, text)
print("Text:", text)
print("Pattern:", pattern)

if result:
    print("Match found:", result.group())
else:
    print("No match")

# Explanation:
# ^Python means the string must start with 'Python'


print("\n==============================")
print("3. DOLLAR ($) → End of string")
print("==============================")

text = "I love Python"
pattern = r"Python$"

result = re.search(pattern, text)
print("Text:", text)
print("Pattern:", pattern)

if result:
    print("Match found:", result.group())
else:
    print("No match")

# Explanation:
# Python$ means the string must end with 'Python'


print("\n==============================")
print("4. STAR (*) → 0 or more occurrences")
print("==============================")

text = "color colour colouur"
pattern = r"colou*r"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# u* → zero or more 'u'
# Matches color, colour, colouur


print("\n==============================")
print("5. PLUS (+) → 1 or more occurrences")
print("==============================")

text = "go goo gooo g"
pattern = r"go+"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# o+ → one or more 'o'
# 'g' alone is NOT matched


print("\n==============================")
print("6. QUESTION MARK (?) → 0 or 1 occurrence")
print("==============================")

text = "color colour"
pattern = r"colou?r"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# u? → 'u' is optional


print("\n==============================")
print("7. CURLY BRACES ({}) → Exact count")
print("==============================")

text = "111 11 1"
pattern = r"\d{2}"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# \d    → digit
# {2}   → exactly two digits


print("\n==============================")
print("8. CHARACTER SET ([])")
print("==============================")

text = "bat cat rat mat"
pattern = r"[bcr]at"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# [bcr] → b OR c OR r


print("\n==============================")
print("9. GROUPING (())")
print("==============================")

text = "abc123 xyz456"
pattern = r"([a-z]+)(\d+)"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# () captures parts of the match
# First group → letters
# Second group → digits


print("\n==============================")
print("10. OR (|)")
print("==============================")

text = "cat dog bat rat"
pattern = r"cat|dog"

result = re.findall(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Matches:", result)

# Explanation:
# cat|dog → match either 'cat' OR 'dog'


print("\n==============================")
print("11. ESCAPE (\\)")
print("==============================")

text = "3 + 5 = 8"
pattern = r"\+"

result = re.search(pattern, text)
print("Text:", text)
print("Pattern:", pattern)
print("Match:", result.group())

# Explanation:
# + is special in regex
# \+ means match literal '+'


print("\n==============================")
print("12. SUBSTITUTION USING re.sub()")
print("==============================")

text = "My phone number is 987654"
pattern = r"\d"
replacement = "X"

result = re.sub(pattern, replacement, text)
print("Text:", text)
print("Pattern:", pattern)
print("Result:", result)

# Explanation:
# \d → digit
# Replaces every digit with 'X'


print("\n==============================")
print("END OF REGEX DEMO")
print("==============================")
