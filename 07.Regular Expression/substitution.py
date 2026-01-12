"""
====================================================
SUBSTITUTING PATTERNS IN REGEX (re.sub & re.subn)
====================================================

This file explains:
- What substitution means
- How re.sub() works
- How re.subn() works
- Using groups in replacement
- Real-world text cleaning examples

Audience: Beginners
"""

import re


print("\n===================================")
print("1. BASIC re.sub()")
print("===================================")

text = "My phone number is 9876543210"
pattern = r"\d"
replacement = "X"

result = re.sub(pattern, replacement, text)
print("Text:", text)
print("Pattern:", pattern)
print("Replacement:", replacement)
print("Result:", result)

# Explanation:
# \d → digit
# Every digit is replaced with 'X'


print("\n===================================")
print("2. REPLACING WORDS")
print("===================================")

text = "I love Python. Python is powerful."
pattern = r"Python"
replacement = "JavaScript"

result = re.sub(pattern, replacement, text)
print("Text:", text)
print("Result:", result)

# Explanation:
# All occurrences of 'Python' are replaced


print("\n===================================")
print("3. LIMITING REPLACEMENTS (count)")
print("===================================")

result = re.sub(pattern, replacement, text, count=1)
print("Replace only first match:", result)

# Explanation:
# count=1 → only first occurrence is replaced


print("\n===================================")
print("4. USING GROUPS IN SUBSTITUTION")
print("===================================")

text = "abc123 xyz456"
pattern = r"([a-z]+)(\d+)"
replacement = r"\2-\1"

result = re.sub(pattern, replacement, text)
print("Text:", text)
print("Pattern:", pattern)
print("Replacement:", replacement)
print("Result:", result)

# Explanation:
# () → capturing groups
# \1 → first group
# \2 → second group
# Order is reversed


print("\n===================================")
print("5. REMOVING UNWANTED CHARACTERS")
print("===================================")

text = "Hello@World#Python!"
pattern = r"\W"
replacement = ""

result = re.sub(pattern, replacement, text)
print("Text:", text)
print("Result:", result)

# Explanation:
# \W → non-word characters
# Used to clean text


print("\n===================================")
print("6. MULTIPLE SPACES TO SINGLE SPACE")
print("===================================")

text = "This    is   Python     Regex"
pattern = r"\s+"
replacement = " "

result = re.sub(pattern, replacement, text)
print("Before:", repr(text))
print("After :", repr(result))

# Explanation:
# \s+ → one or more whitespace
# Converts multiple spaces into one


print("\n===================================")
print("7. USING re.sub() WITH FUNCTION")
print("===================================")


def square(match):
    number = int(match.group())
    return str(number * number)


text = "Numbers: 2 3 4"
pattern = r"\d"

result = re.sub(pattern, square, text)
print("Text:", text)
print("Result:", result)

# Explanation:
# Instead of string replacement,
# a FUNCTION is used
# match.group() gives matched text


print("\n===================================")
print("8. re.subn() → SUBSTITUTION + COUNT")
print("===================================")

text = "Error 404, Error 500, Error 403"
pattern = r"Error"
replacement = "Warning"

result, count = re.subn(pattern, replacement, text)
print("Text:", text)
print("Result:", result)
print("Replacements made:", count)

# Explanation:
# re.subn() returns:
# (new_string, number_of_replacements)


print("\n===================================")
print("9. CASE-INSENSITIVE SUBSTITUTION")
print("===================================")

text = "python Python PYTHON"
pattern = r"python"
replacement = "Java"

result = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print("Text:", text)
print("Result:", result)

# Explanation:
# IGNORECASE flag ignores case


print("\n===================================")
print("10. REAL-WORLD EXAMPLE: MASK EMAIL")
print("===================================")

text = "Contact: user123@gmail.com"
pattern = r"([a-zA-Z0-9._%+-]+)@"
replacement = r"****@"

result = re.sub(pattern, replacement, text)
print("Text:", text)
print("Result:", result)

# Explanation:
# Masks username part of email


print("\n===================================")
print("SUMMARY")
print("===================================")

print(
    """
re.sub(pattern, replacement, text)
- Replaces matches
- Returns new string

re.subn(pattern, replacement, text)
- Replaces matches
- Returns (string, count)

Replacement can be:
- String
- Group reference (\\1, \\2)
- Function
"""
)

print("\n==============================")
print("END OF SUBSTITUTION DEMO")
print("==============================")
